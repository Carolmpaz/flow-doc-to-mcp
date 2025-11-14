FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar FastMCP
RUN pip install --no-cache-dir fastmcp

# Copiar código da aplicação
COPY . .

# Criar diretório para servidores MCP
RUN mkdir -p /app/mcp_servers

# Expor porta do gateway
EXPOSE 8000

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV MCP_GATEWAY_PORT=8000

# Comando padrão (pode ser sobrescrito)
CMD ["python", "gateway_server.py"]

