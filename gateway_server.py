#!/usr/bin/env python3
"""
Servidor HTTP para o MCP Gateway
Expõe os servidores MCP via API REST
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import json
import subprocess
import sys
from pathlib import Path
import uvicorn

app = FastAPI(title="MCP Gateway API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MCP_SERVERS_DIR = Path("./mcp_servers")
MCP_SERVERS_PATTERN = "mcp_servers_*"
REGISTRY_FILE = Path("./mcp_registry.json")

class ServerInfo(BaseModel):
    name: str
    path: str
    directory: str
    timestamp: Optional[str] = None

class ToolCall(BaseModel):
    server_name: str
    tool_name: str
    arguments: Dict

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

@app.get("/")
async def root():
    return {
        "name": "MCP Gateway",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "servers": "/api/servers",
            "discover": "/api/discover",
            "call": "/api/call"
        }
    }

@app.get("/api/servers", response_model=List[ServerInfo])
async def list_servers():
    """Lista todos os servidores MCP registrados"""
    registry = load_registry()
    return registry.get("servers", [])

@app.post("/api/discover")
async def discover_servers():
    """Descobre e registra novos servidores MCP"""
    discovered = discover_mcp_servers()
    registry = load_registry()
    
    registered_names = {s["name"] for s in registry["servers"]}
    new_servers = []
    
    for server in discovered:
        if server["name"] not in registered_names:
            registry["servers"].append(server)
            new_servers.append(server)
    
    if new_servers:
        save_registry(registry)
    
    return {
        "discovered": len(discovered),
        "registered": len(registry["servers"]),
        "new": len(new_servers),
        "new_servers": new_servers
    }

@app.get("/api/servers/{server_name}")
async def get_server(server_name: str):
    """Obtém informações de um servidor específico"""
    registry = load_registry()
    
    server = next(
        (s for s in registry["servers"] if s["name"].lower() == server_name.lower()),
        None
    )
    
    if not server:
        raise HTTPException(status_code=404, detail=f"Servidor '{server_name}' não encontrado")
    
    return server

@app.post("/api/call")
async def call_tool(tool_call: ToolCall):
    """Chama uma tool de um servidor MCP"""
    registry = load_registry()
    
    server = next(
        (s for s in registry["servers"] if s["name"].lower() == tool_call.server_name.lower()),
        None
    )
    
    if not server:
        raise HTTPException(status_code=404, detail=f"Servidor '{tool_call.server_name}' não encontrado")
    
    try:
        server_path = server['path']
        
        proc = subprocess.run(
            [sys.executable, server_path],
            input=json.dumps({
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/call",
                "params": {
                    "name": tool_call.tool_name,
                    "arguments": tool_call.arguments
                }
            }).encode(),
            capture_output=True,
            timeout=30
        )
        
        if proc.returncode == 0:
            response = json.loads(proc.stdout.decode())
            return response
        else:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao executar tool: {proc.stderr.decode()}"
            )
    
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Timeout ao executar tool")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    print("Iniciando MCP Gateway Server...")
    
    registry = load_registry()
    if not registry.get("servers"):
        print("Descobrindo servidores MCP...")
        discovered = discover_mcp_servers()
        if discovered:
            save_registry({"servers": discovered})
            print(f"{len(discovered)} servidor(es) MCP descoberto(s)")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)

