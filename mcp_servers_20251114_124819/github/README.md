# GitHub MCP Server (FastMCP)

Gerado automaticamente com **488 tools**.

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
{
  "mcpServers": {
    "github": {
      "command": "python",
      "args": ["C:\Users\Inteli\Desktop\adapta\mcp_servers_20251114_124819\github/server.py"],
      "env": {
        "GITHUB_TOKEN": "ghp_seu_token_aqui"
      }
    }
  }
}
```

## Endpoints

Total: 488 endpoints da API do GitHub
