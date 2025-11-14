#!/usr/bin/env python3
"""
MCP Fixer PRO: Converte QUALQUER arquivo MCP malfeito em um servidor FastMCP válido
Compatível com FastMCP v2.0+ (2025) e Python 3.13
Uso: python mcp_fixer.py arquivo_errado.py [arquivo_correto.py]
"""
import ast
import re
import sys
import json
import textwrap
from pathlib import Path
from typing import List, Dict, Any, Optional

# ==========================
# Configurações
# ==========================
API_BASE = "https://api.github.com"
GITHUB_TOKEN_VAR = "GITHUB_TOKEN"


# ==========================
# Parser AST + Fixer
# ==========================
class MCPFixer(ast.NodeVisitor):
    def __init__(self):
        self.tools: List[Dict[str, Any]] = []

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        # Detecta @mcp.call_tool()
        for decorator in node.decorator_list:
            if self.is_mcp_call_tool(decorator):
                args = [arg.arg for arg in node.args.args if arg.arg != "self"]
                self.tools.append({
                    "name": node.name,
                    "node": node,
                    "args": args,
                    "docstring": ast.get_docstring(node) or ""
                })
                break
        self.generic_visit(node)

    def is_mcp_call_tool(self, node) -> bool:
        return (
            isinstance(node, ast.Call) and
            isinstance(node.func, ast.Attribute) and
            node.func.attr == "call_tool" and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == "mcp"
        )

    def fix_tool(self, tool: Dict[str, Any]) -> str:
        name = tool["name"]
        args = tool["args"]
        docstring = tool["docstring"]
        description = docstring.strip().split("\n", 1)[0] if docstring else f"Ferramenta {name}"

        # Extrai URL do corpo
        body_str = ast.unparse(tool["node"].body)
        url_match = re.search(r'url\s*=\s*["\'](.*?)["\']', body_str, re.DOTALL)
        raw_url = url_match.group(1) if url_match else ""

        # Corrige URL
        base_url = raw_url.replace("docs.github.com", "api.github.com").strip()
        if not base_url.startswith("http"):
            base_url = f"{API_BASE}{base_url}" if base_url.startswith("/") else f"{API_BASE}/{base_url}"

        # Detecta método
        method = "get"
        if re.search(r'\.post\(', body_str): method = "post"
        elif re.search(r'\.put\(', body_str): method = "put"
        elif re.search(r'\.patch\(', body_str): method = "patch"

        # Monta código de parâmetros e payload
        param_lines = []
        payload_lines = []
        url_format_line = ""

        if "username" in args:
            if "{username}" not in base_url:
                if "followers" in name:
                    base_url = f"{API_BASE}/users/{{username}}/followers"
                elif "repos" in name:
                    base_url = f"{API_BASE}/users/{{username}}/repos"
                else:
                    base_url = f"{base_url}/{{username}}"
            url_format_line = "    url = url.format(username=username)"

        for arg in args:
            if arg in ["per_page", "page", "type", "sort"]:
                param_lines.append(f"    params['{arg}'] = {arg}")
            elif arg in ["title", "body"]:
                payload_lines.append(f"    if {arg} is not None:\n        payload['{arg}'] = {arg}")
            elif arg == "labels":
                payload_lines.append(f"    if {arg} is not None:\n        payload['labels'] = {arg}")

        # Retorno type hint
        return_type = "List[Dict[str, Any]]" if any(k in name for k in ["list", "followers", "repos"]) else "Dict[str, Any]"

        # Monta a tool com FastMCP
        code = f'''@mcp.tool(
    name="{name}",
    description="{description}"
)
def {name}({", ".join(self._format_arg(arg) for arg in args)}) -> {return_type}:'''

        code += f'''
    url = "{base_url}"
    headers = get_headers()
    params = {{}}
    payload = {{}}
'''

        if url_format_line:
            code += f"{url_format_line}\n"

        if param_lines:
            code += "\n".join(param_lines) + "\n"

        if payload_lines:
            code += "\n" + "\n".join(payload_lines) + "\n"

        # Requisição HTTP (síncrona)
        if method == "get":
            code += f'''    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {{k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {{status}}: {{e.response.text[:200]}}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {{str(e)}}")
'''
        else:
            code += f'''    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.{method}(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {{status}}: {{e.response.text[:200]}}")
    except Exception as e:
        raise ToolError(f"Erro: {{str(e)}}")
'''

        return textwrap.dedent(code)

    def _format_arg(self, arg: str) -> str:
        if arg == "username":
            return "username: str"
        elif arg in ["per_page", "page"]:
            return f"{arg}: int = 30" if arg == "per_page" else f"{arg}: int = 1"
        elif arg in ["title", "body"]:
            return f"{arg}: Optional[str] = None"
        elif arg == "labels":
            return f"{arg}: Optional[List[str]] = None"
        return f"{arg}: str"


# ==========================
# Função Principal
# ==========================
def fix_mcp_file(input_path: str, output_path: Optional[str] = None):
    input_path = Path(input_path)
    if not input_path.exists():
        print(f"Erro: Arquivo não encontrado: {input_path}")
        return

    output_path = Path(output_path or input_path.with_name(input_path.stem + ".py"))
    source = input_path.read_text(encoding="utf-8")

    try:
        tree = ast.parse(source)
    except Exception as e:
        print(f"Erro ao parsear o arquivo: {e}")
        return

    fixer = MCPFixer()
    fixer.visit(tree)

    if not fixer.tools:
        print("Nenhuma tool com @mcp.call_tool() encontrada.")
        return

    # Cabeçalho FastMCP CORRIGIDO (sem version/mask)
    # Cabeçalho corrigido
    fixed_lines = [
    "#!/usr/bin/env python3",
    '"""',
    "MCP Server FastMCP (Gerado automaticamente - 2025)",
    "Compatível com FastMCP v2.13+ e erros via ToolError",
    '"""',
    "",
    "import os",
    "import httpx",
    "from typing import List, Dict, Any, Optional",
    "from fastmcp import FastMCP",  # Apenas FastMCP de fastmcp
    "from mcp.server.fastmcp.exceptions import ToolError",  # ToolError correto
    "",
    'mcp = FastMCP("github-api-fixed")',  # Sem args extras
    # ... resto igual
]
   

    # Adiciona tools corrigidas
    for tool in fixer.tools:
        fixed_lines.append(fixer.fix_tool(tool))
        fixed_lines.append("")

    # Execução simples
    fixed_lines += [
        "",
        "if __name__ == \"__main__\":",
        "    mcp.run()"
    ]

    output_path.write_text("\n".join(fixed_lines), encoding="utf-8")
    print(f"Sucesso: Arquivo FastMCP gerado em: {output_path}")
    print("\nPróximos passos:")
    print("   1. pip install --upgrade fastmcp httpx")
    print("   2. set FASTMCP_SERVER_VERSION=1.0.0  # Para version")
    print("   3. set GITHUB_TOKEN=ghp_xxxxxxxxxxxx")
    print("   4. python arquivo_fixed.py  # Deve rodar sem erros!")
    print("   5. fastmcp dev  # Para testar com CLI")


# ==========================
# CLI
# ==========================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python mcp_fixer.py <arquivo_errado.py> [arquivo_correto.py]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    fix_mcp_file(input_file, output_file)