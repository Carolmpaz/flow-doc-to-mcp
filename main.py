#!/usr/bin/env python3
"""
GitHub API Complete Extractor
Extrai TODOS os endpoints (763+) e gera descrições em português
"""
import requests
from bs4 import BeautifulSoup
import re
import json
import os
import time
from typing import List, Dict, Set, Tuple
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin, urlparse

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "")
SONAR_MODEL = "llama-3.1-sonar-large-128k-online"

# Regex para endpoints
ENDPOINT_REGEX = re.compile(
    r'\b(GET|POST|PUT|DELETE|PATCH)\s+(\/[a-zA-Z0-9\-_/]*(?:\{[a-zA-Z0-9_]+\})?[a-zA-Z0-9\-_/]*)\b'
)

# Delay entre requests
DELAY = 0.3
MAX_WORKERS = 3

# ============================================================================
# MODELOS
# ============================================================================

@dataclass
class Parameter:
    name: str
    location: str
    type: str
    required: bool
    description: str = ""

@dataclass
class Endpoint:
    method: str
    path: str
    description: str = ""
    parameters: List[Parameter] = field(default_factory=list)
    source_url: str = ""  # URL onde foi encontrado
    
    @property
    def tool_name(self) -> str:
        """Gera nome da tool"""
        action = {
            "GET": "obter" if "{" in self.path else "listar",
            "POST": "criar",
            "PUT": "atualizar",
            "PATCH": "modificar",
            "DELETE": "deletar"
        }.get(self.method, "chamar")
        
        parts = [p for p in self.path.split('/') if p and not p.startswith('{')]
        if parts:
            resource = '_'.join(parts[-2:] if len(parts) > 1 else parts[-1:])
        else:
            resource = "recurso"
        
        resource = re.sub(r'[^a-z0-9_]', '_', resource.lower())
        resource = re.sub(r'_+', '_', resource).strip('_')
        
        return f"{action}_{resource}"

# ============================================================================
# NAVEGADOR DE PÁGINAS DO GITHUB
# ============================================================================

class GitHubDocsNavigator:
    """Navega pela documentação do GitHub para encontrar TODAS as páginas"""
    
    def __init__(self):
        self.visited: Set[str] = set()
        self.base_url = "https://docs.github.com"
    
    def find_all_api_pages(self, start_url: str) -> List[str]:
        """Encontra TODAS as páginas de referência da API explorando recursivamente"""
        print("🔍 Navegando pela documentação do GitHub...")
        
        all_pages = self._crawl_recursive(start_url)
        
        print(f"\n✅ Total: {len(all_pages)} páginas de API encontradas")
        
        return all_pages
    
    def _crawl_recursive(self, page_url: str) -> List[str]:
        """Explora recursivamente todas as páginas vinculadas que parecem conter endpoints"""
        if page_url in self.visited:
            return []
        
        print(f"   Visitando: {page_url}")
        self.visited.add(page_url)
        pages = [page_url]
        
        try:
            response = requests.get(page_url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(self.base_url, href.split('#')[0])
                
                # Considera somente links dentro da documentação REST do GitHub
                if (full_url.startswith(self.base_url + "/en/rest") and
                    full_url not in self.visited):
                    # Exclui páginas de referência se quiser evitar (opcional)
                    if '/reference/' not in full_url:
                        pages.extend(self._crawl_recursive(full_url))
        
        except Exception as e:
            print(f"  ⚠️ Erro ao acessar {page_url}: {e}")
        
        return pages


    def _crawl_section(self, section_url: str) -> List[str]:
        """Extrai todas as páginas de uma seção"""
        if section_url in self.visited:
            return []
        
        self.visited.add(section_url)
        pages = [section_url]
        
        try:
            response = requests.get(section_url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Procura links para sub-páginas de referência
            for link in soup.find_all('a', href=True):
                href = link['href']
                
                # Filtra apenas links de referência de API
                if '/rest/' in href and '/reference/' not in href:
                    full_url = urljoin(self.base_url, href)
                    
                    # Remove âncoras
                    full_url = full_url.split('#')[0]
                    
                    # Adiciona se ainda não visitou
                    if full_url not in self.visited and '/rest/' in full_url:
                        pages.append(full_url)
                        self.visited.add(full_url)
        
        except Exception as e:
            print(f"  ⚠️ Erro em {section_url}: {e}")
        
        return pages

# ============================================================================
# EXTRATOR DE ENDPOINTS
# ============================================================================

def extract_endpoints_from_page(url: str) -> List[Tuple[str, str, str]]:
    """Extrai endpoints de uma página"""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Procura em blocos de código e tabelas
        blocks = soup.find_all(['pre', 'code', 'table', 'div'])
        
        endpoints = []
        seen = set()
        
        for block in blocks:
            text = ' '.join(block.get_text().split())
            
            for match in ENDPOINT_REGEX.finditer(text):
                method = match.group(1)
                path = match.group(2).rstrip('/')
                
                # Limpa path
                path = re.sub(r'(GET|POST|PUT|DELETE|PATCH)$', '', path)
                
                key = (method, path)
                if key in seen or len(path) < 3:
                    continue
                
                seen.add(key)
                
                # Contexto
                start = max(0, match.start() - 200)
                end = min(len(text), match.end() + 200)
                context = text[start:end]
                
                endpoints.append((method, path, context))
        
        return endpoints
    
    except Exception as e:
        return []

# ============================================================================
# GERADOR DE DESCRIÇÕES EM PORTUGUÊS
# ============================================================================

class DescriptionGenerator:
    """Generate endpoint descriptions in English using Perplexity"""

    def __init__(self, api_key: str, tool_name: str):
        self.api_key = api_key
        self.tool_name = tool_name
        self.cache = {}  # Cache to avoid repeated requests

    def generate_description(self, method: str, path: str, context: str) -> str:
        """Generate description in English"""

        cache_key = f"{method}:{path}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        if not self.api_key:
            return self._fallback_description(method, path)

        prompt = f"""Analyze this API endpoint and generate a concise English description.

METHOD: {method}
PATH: {path}
CONTEXT: {context[:300]}

Rules:
1. Use English
2. Be specific about what the endpoint does
3. Mention the tool name '{self.tool_name}' at the beginning
4. Use action verbs: "Get", "List", "Create", "Update", "Delete"
5. Maximum 80 characters

Examples:
- GET /users/{{username}}: "Get detailed information of a user in {self.tool_name}"
- POST /repos/{{owner}}/{{repo}}/issues: "Create a new issue in a repository of {self.tool_name}"
- DELETE /orgs/{{org}}/members/{{username}}: "Delete a member from an organization in {self.tool_name}"

Return ONLY the description, without quotes or formatting."""

        try:
            response = requests.post(
                "https://api.perplexity.ai/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": SONAR_MODEL,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.2,
                    "max_tokens": 100
                },
                timeout=20
            )

            if response.ok:
                result = response.json()
                description = result["choices"][0]["message"]["content"].strip()
                description = description.strip('"\'')
                self.cache[cache_key] = description
                return description

        except:
            pass

        return self._fallback_description(method, path)

    def _fallback_description(self, method: str, path: str) -> str:
        """Fallback description in English"""

        action_map = {
            "GET": "Get",
            "POST": "Create",
            "PUT": "Update",
            "PATCH": "Modify",
            "DELETE": "Delete"
        }
        action = action_map.get(method, method)

        parts = [p for p in path.split('/') if p and not p.startswith('{')]

        if parts:
            resource = parts[-1].replace('-', ' ').replace('_', ' ')
        else:
            resource = "resource"

        if "{" in path:
            return f"{action} {resource} in {self.tool_name}"
        else:
            return f"{action} list of {resource} in {self.tool_name}"


# ============================================================================
# ENRIQUECEDOR DE ENDPOINTS
# ============================================================================

class EndpointEnricher:
    """Enrich endpoints with parameters and descriptions using Perplexity"""

    def __init__(self, api_key: str, tool_name: str):
        self.api_key = api_key
        self.desc_generator = DescriptionGenerator(api_key, tool_name)

    def enrich(self, method: str, path: str, context: str, source_url: str) -> Endpoint:
        description = self.desc_generator.generate_description(method, path, context)
        parameters = self._extract_parameters(path, context)
        return Endpoint(method=method, path=path, description=description, parameters=parameters, source_url=source_url)

    def _extract_parameters(self, path: str, context: str) -> List[Parameter]:
        """Extract parameters from path and context"""
        params = []
        seen = set()

        # Path parameters
        for match in re.finditer(r'\{([a-zA-Z0-9_]+)\}', path):
            param_name = match.group(1)

            if param_name not in seen:
                seen.add(param_name)

                desc_map = {
                    'username': 'GitHub username',
                    'org': 'Organization name',
                    'owner': 'Repository owner',
                    'repo': 'Repository name',
                    'id': 'Unique identifier',
                    'number': 'Item number',
                    'name': 'Resource name'
                }

                description = desc_map.get(param_name, f'The {param_name}')

                params.append(Parameter(
                    name=param_name,
                    location="path",
                    type="string",
                    required=True,
                    description=description
                ))

        # Common query parameters
        common_query_params = {
            'page': ('integer', 'Page number for pagination'),
            'per_page': ('integer', 'Items per page (max 100)'),
            'since': ('string', 'Filter results after this date'),
            'state': ('string', 'Resource state (open, closed, all)'),
            'sort': ('string', 'Field to sort by'),
            'direction': ('string', 'Sort direction (asc, desc)')
        }

        for param_name, (param_type, param_desc) in common_query_params.items():
            if param_name.lower() in context.lower() and param_name not in seen:
                seen.add(param_name)
                params.append(Parameter(
                    name=param_name,
                    location="query",
                    type=param_type,
                    required=False,
                    description=param_desc
                ))

        return params


# ============================================================================
# GERADOR DE MCP
# ============================================================================

class MCPGenerator:
    """Gera MCP Server"""
    
    def __init__(self, api_name: str, base_url: str):
        self.api_name = api_name
        self.base_url = base_url
        self.function_names: Set[str] = set()
    
    def generate(self, endpoints: List[Endpoint], output_dir: str = "./mcp_servers") -> Path:
        """Gera servidor MCP"""
        
        name_clean = re.sub(r'[^a-z0-9_]', '_', self.api_name.lower())
        server_dir = Path(output_dir) / name_clean
        server_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n🔧 Gerando MCP com {len(endpoints)} tools...")
        
        # Gera tools
        tools = []
        for endpoint in endpoints:
            tool_code = self._generate_tool(endpoint)
            if tool_code:
                tools.append(tool_code)
        
        # Servidor
        server_code = f'''#!/usr/bin/env python3
"""
MCP Server para API do GitHub
Gerado automaticamente em: {time.strftime("%Y-%m-%d %H:%M:%S")}
Total de tools: {len(tools)}
"""
import os
import httpx
from typing import Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server

mcp = Server("github-api")
BASE_URL = "{self.base_url}"

def get_headers():
    """Obtém headers de autenticação"""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN não configurada")
    return {{
        "Authorization": f"Bearer {{token}}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }}


{chr(10).join(tools)}


async def main():
    """Inicia o servidor MCP"""
    async with stdio_server() as (read, write):
        await mcp.run(read, write, mcp.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
'''
        
        (server_dir / "server.py").write_text(server_code, encoding='utf-8')
        (server_dir / "requirements.txt").write_text("httpx>=0.24.0\nmcp>=0.1.0\n")
        
        # README em português
        (server_dir / "README.md").write_text(f"""# Servidor MCP para GitHub API

Servidor MCP gerado automaticamente com **{len(tools)} tools** da API do GitHub.

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

```bash
export GITHUB_TOKEN='ghp_seu_token_aqui'
```

## Uso

```bash
python server.py
```

## Integração com Claude Desktop

Adicione ao `claude_desktop_config.json`:

```json
{{
  "mcpServers": {{
    "github": {{
      "command": "python",
      "args": ["{server_dir.absolute()}/server.py"],
      "env": {{
        "GITHUB_TOKEN": "ghp_seu_token_aqui"
      }}
    }}
  }}
}}
```

## Endpoints

Total: {len(endpoints)} endpoints da API do GitHub
""", encoding='utf-8')
        
        print(f"✅ MCP gerado: {server_dir}/")
        print(f"   Tools: {len(tools)}")
        
        return server_dir
    
    def _generate_tool(self, endpoint: Endpoint) -> str:
        """Gera código de uma tool"""
        
        # Nome único
        base_name = endpoint.tool_name
        func_name = base_name
        counter = 2
        while func_name in self.function_names:
            func_name = f"{base_name}_{counter}"
            counter += 1
        self.function_names.add(func_name)
        
        # Parâmetros
        path_params = [p for p in endpoint.parameters if p.location == "path"]
        query_params = [p for p in endpoint.parameters if p.location == "query"]
        
        sig_parts = []
        for p in path_params:
            pname = self._sanitize_name(p.name)
            sig_parts.append(f"{pname}: str")
        
        for p in query_params:
            pname = self._sanitize_name(p.name)
            sig_parts.append(f"{pname}: Optional[str] = None")
        
        signature = ", ".join(sig_parts) if sig_parts else ""
        
        # Docstring
        doc_lines = [f'"""{endpoint.description}']
        if endpoint.parameters:
            doc_lines.append("    ")
            doc_lines.append("    Args:")
            for p in endpoint.parameters:
                pname = self._sanitize_name(p.name)
                doc_lines.append(f"        {pname}: {p.description}")
        doc_lines.append('    """')
        
        # Corpo
        url_template = f'"{self.base_url}{endpoint.path}"'
        if path_params:
            url_template = f'f"{self.base_url}{endpoint.path}"'
        
        lines = [
            "@mcp.call_tool()",
            f"async def {func_name}({signature}) -> str:",
            "    " + "\n    ".join(doc_lines),
            f"    url = {url_template}",
            "    headers = get_headers()"
        ]
        
        if query_params:
            lines.append("    params = {}")
            for p in query_params:
                pname = self._sanitize_name(p.name)
                lines.append(f"    if {pname} is not None:")
                lines.append(f"        params['{p.name}'] = {pname}")
        
        method = endpoint.method.lower()
        lines.append("    async with httpx.AsyncClient() as client:")
        
        if query_params:
            lines.append(f"        response = await client.{method}(url, headers=headers, params=params)")
        else:
            lines.append(f"        response = await client.{method}(url, headers=headers)")
        
        lines.append("        response.raise_for_status()")
        lines.append("        return response.text")
        
        return "\n".join(lines)
    
    def _sanitize_name(self, name: str) -> str:
        """Sanitiza nome"""
        name = re.sub(r'[^a-z0-9_]', '_', name.lower())
        name = re.sub(r'_+', '_', name).strip('_')
        if not name or name[0].isdigit():
            name = f"param_{name}"
        if name in ['class', 'def', 'return', 'type']:
            name = f"{name}_param"
        return name or "param"

# ============================================================================
# PIPELINE COMPLETO
# ============================================================================


from datetime import datetime

def extract_complete_github_api(start_url: str, output_dir: str = "./mcp_servers", tool_name: str = "MyAPI",
api_base_url: str = ""):
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{output_dir.rstrip('_')}_{timestamp}"

    print("="*70)
    print(f"🚀 COMPLETE EXTRACTION OF {tool_name} API")
    print("="*70)

    # 1. Navega e encontra TODAS as páginas
    navigator = GitHubDocsNavigator()
    all_pages = navigator.find_all_api_pages(start_url)

    # 2. Extrai endpoints
    print(f"\n📄 Extracting endpoints from {len(all_pages)} pages...")

    all_endpoints_raw = []
    for i, page_url in enumerate(all_pages, 1):
        if i % 10 == 0:
            print(f"   [{i}/{len(all_pages)}] Processed...")
        endpoints = extract_endpoints_from_page(page_url)
        for method, path, context in endpoints:
            all_endpoints_raw.append((method, path, context, page_url))
        time.sleep(0.1)

    # Remove duplicatas
    seen = set()
    unique_endpoints = []
    for method, path, context, url in all_endpoints_raw:
        key = (method, path)
        if key not in seen:
            seen.add(key)
            unique_endpoints.append((method, path, context, url))

    print(f"\n✅ {len(unique_endpoints)} unique endpoints found")

    # 3. Enriquece com descrições
    print(f"\n🤖 Enriching with descriptions in English...")

    enricher = EndpointEnricher(PERPLEXITY_API_KEY, tool_name)
    enriched_endpoints = []

    for i, (method, path, context, url) in enumerate(unique_endpoints, 1):
        if i % 50 == 0:
            print(f"   [{i}/{len(unique_endpoints)}] Processed...")
        endpoint = enricher.enrich(method, path, context, url)
        enriched_endpoints.append(endpoint)
        time.sleep(0.2)

    print(f"\n✅ {len(enriched_endpoints)} endpoints enriched")

    # 4. Gera MCP com URL base dinâmica
    if not api_base_url:
        raise ValueError("API base URL must be provided")
    generator = MCPGenerator(tool_name, api_base_url)
    server_dir = generator.generate(enriched_endpoints, output_dir)

    # 5. Resumo final
    print(f"\n{'='*70}")
    print(f"✅ COMPLETED!")
    print(f"{'='*70}")
    print(f"\n📁 Server: {server_dir}/server.py")
    print(f"📦 Tools: {len(enriched_endpoints)}")
    print(f"\n📝 To run:")
    print(f"   1. cd {server_dir}")
    print(f"   2. pip install -r requirements.txt")
    print(f"   3. export GITHUB_TOKEN='your_token_here'")
    print(f"   4. python server.py")

    return server_dir


def main():
    if not PERPLEXITY_API_KEY:
        print("⚠️  PERPLEXITY_API_KEY not set")
        print("   Descriptions will be basic")
        print("   Set with: export PERPLEXITY_API_KEY='pplx-...'\n")

    start_url = input("Enter the API documentation base URL (e.g. https://docs.github.com/en/rest): ").strip()
    tool_name = input("Enter the name for the MCP tool (e.g. GitHub, MyAPI): ").strip() or "MyAPI"
    api_base_url = input("Enter the base URL for the API (e.g. https://api.github.com): ").strip()

    extract_complete_github_api(start_url, tool_name=tool_name, api_base_url=api_base_url)



if __name__ == "__main__":
    main()