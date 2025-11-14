# Flow - API Extractor & MCP Generator

Sistema completo para extrair endpoints de APIs e gerar servidores MCP automaticamente.

## 🚀 Funcionalidades

- Interface web intuitiva para configurar extrações
- Armazenamento de requisições no banco de dados PostgreSQL
- Processamento automático em background (worker)
- Acompanhamento de status em tempo real
- Histórico de todas as extrações

## 📋 Pré-requisitos

- Python 3.8+
- PostgreSQL (Supabase)
- Chave da API Perplexity (opcional, configurada no backend)

## 🔧 Instalação

1. Clone o repositório ou navegue até a pasta do projeto

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a variável de ambiente do banco de dados:


4. (Opcional) Configure a chave da API Perplexity no backend:
```bash
export PERPLEXITY_API_KEY='pplx-...'
```

## 🎯 Uso

1. Inicie o servidor:
```bash
python app.py
```

2. Acesse a interface web:
```
http://localhost:5000
```

3. Preencha os campos:
   - **URL da Documentação da API**: URL base da documentação (ex: https://docs.github.com/en/rest)
   - **Nome da Ferramenta MCP**: Nome para identificar a ferramenta (ex: GitHub, MyAPI)
   - **URL Base da API**: URL base da API (ex: https://api.github.com)

4. Clique em "Gerar MCP Server"

5. Acompanhe o status em tempo real na interface

## 📊 Estrutura do Banco de Dados

A tabela `api_extractions` armazena:
- `id`: ID único da extração
- `start_url`: URL da documentação
- `tool_name`: Nome da ferramenta
- `api_base_url`: URL base da API
- `status`: Status (pending, processing, completed, failed)
- `output_path`: Caminho do servidor MCP gerado
- `error_message`: Mensagem de erro (se houver)
- `endpoint_count`: Número de endpoints encontrados
- `created_at`: Data de criação
- `updated_at`: Data de atualização
- `processed_at`: Data de processamento

## 🔄 Como Funciona

1. **Frontend**: Usuário preenche o formulário e envia
2. **API**: Cria um registro no banco de dados com status "pending"
3. **Worker**: Verifica periodicamente por novas extrações pendentes
4. **Processamento**: Para cada extração pendente, executa o `main.py`
5. **Atualização**: Atualiza o status no banco de dados
6. **Frontend**: Faz polling para mostrar o status atualizado

## 📡 Endpoints da API

- `POST /api/extract`: Cria uma nova extração
- `GET /api/extraction/<id>`: Obtém status de uma extração
- `GET /api/extractions`: Lista todas as extrações (com limite)

## 🛠️ Arquivos Principais

- `app.py`: Servidor Flask e rotas da API
- `database.py`: Funções de acesso ao banco de dados
- `worker.py`: Worker que processa extrações em background
- `main.py`: Lógica principal de extração e geração de MCP
- `templates/index.html`: Interface web

## ⚙️ Configuração do Worker

O worker verifica novas extrações a cada 5 segundos (configurável em `worker.py`).

Para processar múltiplas extrações simultaneamente, cada uma roda em uma thread separada.

## 🔒 Segurança

- A senha do banco de dados deve ser configurada via variável de ambiente
- Nunca commite a senha no código
- Use variáveis de ambiente para todas as credenciais

## 📝 Notas

- O processamento pode levar vários minutos dependendo do tamanho da API
- O worker processa até 5 extrações pendentes por vez
- Extrações são processadas em ordem de criação (FIFO)



