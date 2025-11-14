#!/usr/bin/env python3
"""
MCP Gateway usando FastMCP
Integra todos os servidores MCP gerados dinamicamente
"""
import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
try:
    from fastmcp import FastMCP
    mcp = FastMCP("MCP Gateway")
except ImportError:
    print("⚠️  FastMCP não instalado. Use 'pip install fastmcp' ou use gateway_server.py")
    sys.exit(1)
import asyncio

MCP_SERVERS_DIR = Path("./mcp_servers")
MCP_SERVERS_PATTERN = "mcp_servers_*"
REGISTRY_FILE = Path("./mcp_registry.json")

def discover_mcp_servers() -> List[Dict]:
    """Descobre todos os servidores MCP gerados"""
    servers = []
    
    base_dir = Path(".")
    
    for timestamp_dir in sorted(base_dir.glob(MCP_SERVERS_PATTERN), reverse=True):
        if not timestamp_dir.is_dir() or timestamp_dir.name == "mcp_servers_20251114_012905":
            continue
        
        for server_dir in timestamp_dir.iterdir():
            if not server_dir.is_dir():
                continue
            
            server_file = server_dir / "server.py"
            if server_file.exists():
                server_name = server_dir.name
                server_path = str(server_file.absolute())
                
                servers.append({
                    "name": server_name,
                    "path": server_path,
                    "directory": str(server_dir.absolute()),
                    "timestamp": timestamp_dir.name
                })
    
    if MCP_SERVERS_DIR.exists():
        for timestamp_dir in sorted(MCP_SERVERS_DIR.iterdir(), reverse=True):
            if not timestamp_dir.is_dir():
                continue
            
            for server_dir in timestamp_dir.iterdir():
                if not server_dir.is_dir():
                    continue
                
                server_file = server_dir / "server.py"
                if server_file.exists():
                    server_name = server_dir.name
                    server_path = str(server_file.absolute())
                    
                    servers.append({
                        "name": server_name,
                        "path": server_path,
                        "directory": str(server_dir.absolute()),
                        "timestamp": timestamp_dir.name
                    })
    
    return servers

def load_registry() -> Dict:
    """Carrega o registro de servidores MCP"""
    if REGISTRY_FILE.exists():
        try:
            with open(REGISTRY_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"servers": []}

def save_registry(registry: Dict):
    """Salva o registro de servidores MCP"""
    with open(REGISTRY_FILE, 'w') as f:
        json.dump(registry, f, indent=2)

def register_mcp_server(server_info: Dict):
    """Registra um servidor MCP no gateway"""
    registry = load_registry()
    
    existing = next(
        (s for s in registry["servers"] if s["name"] == server_info["name"]),
        None
    )
    
    if existing:
        existing.update(server_info)
    else:
        registry["servers"].append(server_info)
    
    save_registry(registry)

def auto_discover_and_register():
    """Descobre e registra automaticamente todos os servidores MCP"""
    discovered = discover_mcp_servers()
    registry = load_registry()
    
    registered_names = {s["name"] for s in registry["servers"]}
    
    for server in discovered:
        if server["name"] not in registered_names:
            register_mcp_server(server)
            print(f"Registrado: {server['name']} ({server['path']})")
    
    return load_registry()

@mcp.tool()
def list_mcp_servers() -> str:
    """Lista todos os servidores MCP registrados no gateway"""
    registry = load_registry()
    
    if not registry["servers"]:
        return "Nenhum servidor MCP registrado."
    
    result = f"Servidores MCP registrados ({len(registry['servers'])}):\n\n"
    for i, server in enumerate(registry["servers"], 1):
        result += f"{i}. {server['name']}\n"
        result += f"   Caminho: {server['path']}\n"
        result += f"   Timestamp: {server.get('timestamp', 'N/A')}\n\n"
    
    return result

@mcp.tool()
def discover_new_servers() -> str:
    """Descobre e registra novos servidores MCP automaticamente"""
    registry_before = len(load_registry()["servers"])
    auto_discover_and_register()
    registry_after = len(load_registry()["servers"])
    
    new_count = registry_after - registry_before
    
    if new_count > 0:
        return f"{new_count} novo(s) servidor(es) MCP descoberto(s) e registrado(s)!"
    else:
        return "Nenhum novo servidor MCP encontrado."

@mcp.tool()
def get_server_info(server_name: str) -> str:
    """Obtém informações detalhadas de um servidor MCP específico"""
    registry = load_registry()
    
    server = next(
        (s for s in registry["servers"] if s["name"].lower() == server_name.lower()),
        None
    )
    
    if not server:
        return f"Servidor '{server_name}' não encontrado."
    
    result = f"Informações do servidor: {server['name']}\n\n"
    result += f"Caminho: {server['path']}\n"
    result += f"Diretório: {server['directory']}\n"
    result += f"Timestamp: {server.get('timestamp', 'N/A')}\n"
    
    server_dir = Path(server['directory'])
    readme_file = server_dir / "README.md"
    if readme_file.exists():
        result += f"\nREADME disponível em: {readme_file}\n"
    
    return result

async def proxy_to_server(server_name: str, tool_name: str, arguments: Dict) -> str:
    """Proxy para chamar uma tool de um servidor MCP específico"""
    registry = load_registry()
    
    server = next(
        (s for s in registry["servers"] if s["name"].lower() == server_name.lower()),
        None
    )
    
    if not server:
        return f"Erro: Servidor '{server_name}' não encontrado."
    
    server_path = server['path']
    
    try:
        env = os.environ.copy()
        
        proc = await asyncio.create_subprocess_exec(
            sys.executable,
            server_path,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env
        )
        
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }
        
        stdout, stderr = await proc.communicate(json.dumps(request).encode())
        
        if proc.returncode == 0:
            response = json.loads(stdout.decode())
            return json.dumps(response, indent=2)
        else:
            return f"Erro ao executar tool: {stderr.decode()}"
    
    except Exception as e:
        return f"Erro ao conectar com servidor: {str(e)}"

def create_dynamic_tools():
    """Cria tools dinâmicas baseadas nos servidores MCP registrados"""
    registry = load_registry()
    
    for server in registry["servers"]:
        server_name = server["name"]
        
        @mcp.tool(name=f"call_{server_name}")
        async def call_server_tool(tool_name: str, arguments: str = "{}") -> str:
            """Chama uma tool de um servidor MCP específico"""
            try:
                args_dict = json.loads(arguments) if isinstance(arguments, str) else arguments
                return await proxy_to_server(server_name, tool_name, args_dict)
            except Exception as e:
                return f"Erro: {str(e)}"
        
        call_server_tool.__name__ = f"call_{server_name}_tool"
        call_server_tool.__doc__ = f"Chama tools do servidor MCP '{server_name}'"

if __name__ == "__main__":
    print("Iniciando MCP Gateway com FastMCP...")
    print("Descobrindo servidores MCP...")
    
    auto_discover_and_register()
    
    registry = load_registry()
    print(f"{len(registry['servers'])} servidor(es) MCP registrado(s)")
    
    create_dynamic_tools()
    
    print("Gateway MCP pronto!")
    print("Use as tools 'list_mcp_servers' e 'discover_new_servers' para gerenciar servidores")
    
    mcp.run()

