#!/usr/bin/env python3
"""
MCP Server FastMCP (Gerado automaticamente - 2025)
Compatível com FastMCP v2.0+ e erros via ToolError
"""

import os
import httpx
from typing import List, Dict, Any, Optional
from fastmcp import FastMCP
from mcp.server.fastmcp.exceptions import ToolError  
mcp = FastMCP("github-api-fixed")
API_BASE = "https://api.github.com"

def get_headers() -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("Variável GITHUB_TOKEN não configurada")
    return {
        "Authorization": f"token {{token}}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

@mcp.tool(
    name="listar_repos",
    description="Get list of repos in GitHub"
)
def listar_repos() -> List[Dict[str, Any]]:
    url = "https://api.github.com/repos"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_followers",
    description="Get list of followers in GitHub"
)
def listar_user_followers() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/followers"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_followers",
    description="Get followers in GitHub"
)
def obter_users_followers(username: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/users/{username}/followers"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_spoon_knife_issues",
    description="Create list of issues in GitHub"
)
def criar_spoon_knife_issues() -> Dict[str, Any]:
    url = "https://api.github.com/repos/octocat/Spoon-Knife/issues"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_octocat",
    description="Get list of octocat in GitHub"
)
def listar_octocat() -> List[Dict[str, Any]]:
    url = "https://api.github.com/octocat"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_events",
    description="Get list of events in GitHub"
)
def listar_events(page: int = 1, per_page: int = 30) -> List[Dict[str, Any]]:
    url = "https://api.github.com/events"
    headers = get_headers()
    params = {}
    payload = {}
    params['page'] = page
    params['per_page'] = per_page
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_repos",
    description="Create list of repos in GitHub"
)
def criar_repos() -> List[Dict[str, Any]]:
    url = "https://api.github.com/repos"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_spoon_knife_issues",
    description="Get list of issues in GitHub"
)
def listar_spoon_knife_issues(page: int = 1, per_page: int = 30) -> List[Dict[str, Any]]:
    url = "https://api.github.com/repos/octocat/Spoon-Knife/issues"
    headers = get_headers()
    params = {}
    payload = {}
    params['page'] = page
    params['per_page'] = per_page
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_repo_name_issues",
    description="Get list of issues in GitHub"
)
def listar_repo_name_issues(page: int = 1, per_page: int = 30) -> List[Dict[str, Any]]:
    url = "https://api.github.com/repos/REPO-OWNER/REPO-NAME/issues"
    headers = get_headers()
    params = {}
    payload = {}
    params['page'] = page
    params['per_page'] = per_page
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_rate_limit",
    description="Get list of rate limit in GitHub"
)
def listar_rate_limit() -> List[Dict[str, Any]]:
    url = "https://api.github.com/rate_limit"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_images_custom",
    description="Delete custom in GitHub"
)
def deletar_images_custom(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_images_custom",
    description="Get custom in GitHub"
)
def obter_images_custom(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_images_github_owned",
    description="Get github owned in GitHub"
)
def obter_images_github_owned(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_actions_hosted_runners",
    description="Modify hosted runners in GitHub"
)
def modificar_actions_hosted_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_actions_hosted_runners",
    description="Delete hosted runners in GitHub"
)
def deletar_actions_hosted_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_customization_sub",
    description="Get sub in GitHub"
)
def obter_customization_sub(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_permissions_repositories",
    description="Delete repositories in GitHub"
)
def deletar_permissions_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_permissions_selected_actions",
    description="Get selected actions in GitHub"
)
def obter_permissions_selected_actions(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_self_hosted_runners_repositories",
    description="Delete repositories in GitHub"
)
def deletar_self_hosted_runners_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_permissions_workflow",
    description="Get workflow in GitHub"
)
def obter_permissions_workflow(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_actions_runner_groups",
    description="Modify runner groups in GitHub"
)
def modificar_actions_runner_groups(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_actions_runner_groups",
    description="Delete runner groups in GitHub"
)
def deletar_actions_runner_groups(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_runner_groups",
    description="Get runner groups in GitHub"
)
def obter_actions_runner_groups(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_runners",
    description="Get runners in GitHub"
)
def obter_actions_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_actions_runners",
    description="Delete runners in GitHub"
)
def deletar_actions_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_secrets",
    description="Get secrets in GitHub"
)
def obter_actions_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_actions_secrets",
    description="Update secrets in GitHub"
)
def atualizar_actions_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_actions_secrets",
    description="Delete secrets in GitHub"
)
def deletar_actions_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_variables",
    description="Get variables in GitHub"
)
def obter_actions_variables(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_actions_variables",
    description="Modify variables in GitHub"
)
def modificar_actions_variables(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_actions_variables",
    description="Delete variables in GitHub"
)
def deletar_actions_variables(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_repos",
    description="Delete list of repos in GitHub"
)
def deletar_repos() -> List[Dict[str, Any]]:
    url = "https://api.github.com/repos"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_repos",
    description="Update list of repos in GitHub"
)
def atualizar_repos() -> List[Dict[str, Any]]:
    url = "https://api.github.com/repos"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_repos",
    description="Modify list of repos in GitHub"
)
def modificar_repos() -> List[Dict[str, Any]]:
    url = "https://api.github.com/repos"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_installation_repositories",
    description="Get list of repositories in GitHub"
)
def listar_installation_repositories() -> List[Dict[str, Any]]:
    url = "https://api.github.com/installation/repositories"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_billing_budgets",
    description="Modify budgets in GitHub"
)
def modificar_billing_budgets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_billing_budgets",
    description="Delete budgets in GitHub"
)
def deletar_billing_budgets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_premium_request_usage",
    description="Get usage in GitHub"
)
def obter_premium_request_usage(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_orgs_campaigns",
    description="Modify campaigns in GitHub"
)
def modificar_orgs_campaigns(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_campaigns",
    description="Delete campaigns in GitHub"
)
def deletar_orgs_campaigns(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_code_security_configurations",
    description="Modify configurations in GitHub"
)
def modificar_code_security_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_code_security_configurations",
    description="Delete configurations in GitHub"
)
def deletar_code_security_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_code_security_configurations",
    description="Create configurations in GitHub"
)
def criar_code_security_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_codespaces_secrets",
    description="Update secrets in GitHub"
)
def atualizar_codespaces_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_codespaces_secrets",
    description="Delete secrets in GitHub"
)
def deletar_codespaces_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_codespaces_secrets",
    description="Get secrets in GitHub"
)
def obter_codespaces_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_members",
    description="Get members in GitHub"
)
def obter_orgs_members(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_members",
    description="Create members in GitHub"
)
def criar_orgs_members(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_dependabot_secrets",
    description="Update secrets in GitHub"
)
def atualizar_dependabot_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_dependabot_secrets",
    description="Delete secrets in GitHub"
)
def deletar_dependabot_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_dependabot_secrets",
    description="Get secrets in GitHub"
)
def obter_dependabot_secrets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_meta",
    description="Get list of meta in GitHub"
)
def listar_meta() -> List[Dict[str, Any]]:
    url = "https://api.github.com/meta"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_orgs",
    description="Modify orgs in GitHub"
)
def modificar_orgs(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_metadata_storage_record",
    description="Create storage record in GitHub"
)
def criar_metadata_storage_record(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_attestations_repositories",
    description="Get repositories in GitHub"
)
def obter_attestations_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_attestations",
    description="Get attestations in GitHub"
)
def obter_orgs_attestations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_blocks",
    description="Get blocks in GitHub"
)
def obter_orgs_blocks(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_blocks",
    description="Update blocks in GitHub"
)
def atualizar_orgs_blocks(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_blocks",
    description="Delete blocks in GitHub"
)
def deletar_orgs_blocks(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_failed_invitations",
    description="Get failed invitations in GitHub"
)
def obter_orgs_failed_invitations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_orgs_hooks",
    description="Modify hooks in GitHub"
)
def modificar_orgs_hooks(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_hooks",
    description="Delete hooks in GitHub"
)
def deletar_orgs_hooks(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_hooks",
    description="Get hooks in GitHub"
)
def obter_orgs_hooks(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_hooks",
    description="Create hooks in GitHub"
)
def criar_orgs_hooks(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_api_subject_stats",
    description="Get subject stats in GitHub"
)
def obter_api_subject_stats(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_api_summary_stats",
    description="Get summary stats in GitHub"
)
def obter_api_summary_stats(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_api_time_stats",
    description="Get time stats in GitHub"
)
def obter_api_time_stats(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_api_user_stats",
    description="Get user stats in GitHub"
)
def obter_api_user_stats(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_installations",
    description="Get installations in GitHub"
)
def obter_orgs_installations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_invitations",
    description="Get invitations in GitHub"
)
def obter_orgs_invitations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_orgs_issue_types",
    description="Delete issue types in GitHub"
)
def deletar_orgs_issue_types(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_orgs_members",
    description="Delete members in GitHub"
)
def deletar_orgs_members(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_memberships",
    description="Get memberships in GitHub"
)
def obter_orgs_memberships(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_memberships",
    description="Update memberships in GitHub"
)
def atualizar_orgs_memberships(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_memberships",
    description="Delete memberships in GitHub"
)
def deletar_orgs_memberships(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_organization_roles",
    description="Get organization roles in GitHub"
)
def obter_orgs_organization_roles(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_organization_roles_teams",
    description="Update teams in GitHub"
)
def atualizar_organization_roles_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_organization_roles_teams",
    description="Delete teams in GitHub"
)
def deletar_organization_roles_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_organization_roles_users",
    description="Delete users in GitHub"
)
def deletar_organization_roles_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_organization_roles_users",
    description="Update users in GitHub"
)
def atualizar_organization_roles_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_outside_collaborators",
    description="Delete outside collaborators in GitHub"
)
def deletar_orgs_outside_collaborators(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_personal_access_token_requests",
    description="Get personal access token requests in GitHub"
)
def obter_orgs_personal_access_token_requests(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_personal_access_tokens",
    description="Get personal access tokens in GitHub"
)
def obter_orgs_personal_access_tokens(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_properties_schema",
    description="Update schema in GitHub"
)
def atualizar_properties_schema(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_properties_schema",
    description="Delete schema in GitHub"
)
def deletar_properties_schema(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_properties_values",
    description="Get values in GitHub"
)
def obter_properties_values(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_rulesets",
    description="Get rulesets in GitHub"
)
def obter_orgs_rulesets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_rulesets",
    description="Update rulesets in GitHub"
)
def atualizar_orgs_rulesets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_rulesets",
    description="Delete rulesets in GitHub"
)
def deletar_orgs_rulesets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_security_managers",
    description="Get security managers in GitHub"
)
def obter_orgs_security_managers(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_security_managers_teams",
    description="Delete teams in GitHub"
)
def deletar_security_managers_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_settings_immutable_releases",
    description="Get immutable releases in GitHub"
)
def obter_settings_immutable_releases(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_immutable_releases_repositories",
    description="Delete repositories in GitHub"
)
def deletar_immutable_releases_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_settings_network_configurations",
    description="Get network configurations in GitHub"
)
def obter_settings_network_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_settings_network_configurations",
    description="Modify network configurations in GitHub"
)
def modificar_settings_network_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_settings_network_configurations",
    description="Delete network configurations in GitHub"
)
def deletar_settings_network_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_settings_network_settings",
    description="Get network settings in GitHub"
)
def obter_settings_network_settings(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs",
    description="Create list of orgs in GitHub"
)
def criar_orgs() -> Dict[str, Any]:
    url = "https://api.github.com/orgs"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_users_orgspackages",
    description="Get orgspackages in GitHub"
)
def obter_users_orgspackages(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_orgs_packages",
    description="Delete packages in GitHub"
)
def deletar_orgs_packages(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_packages",
    description="Create packages in GitHub"
)
def criar_orgs_packages(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_packages",
    description="Delete list of packages in GitHub"
)
def deletar_user_packages() -> Dict[str, Any]:
    url = "https://api.github.com/user/packages"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_packages",
    description="Create list of packages in GitHub"
)
def criar_user_packages() -> Dict[str, Any]:
    url = "https://api.github.com/user/packages"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_users_packages",
    description="Delete packages in GitHub"
)
def deletar_users_packages(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_users_packages",
    description="Create packages in GitHub"
)
def criar_users_packages(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_orgs_private_registries",
    description="Modify private registries in GitHub"
)
def modificar_orgs_private_registries(org: str, page: int = 1) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    params['page'] = page
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_private_registries",
    description="Delete private registries in GitHub"
)
def deletar_orgs_private_registries(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_projectsv2",
    description="Create projectsV2 in GitHub"
)
def criar_orgs_projectsv2(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_orgs_projectsv2",
    description="Get projectsV2 in GitHub"
)
def obter_orgs_projectsv2(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_orgs_projectsv2",
    description="Modify projectsV2 in GitHub"
)
def modificar_orgs_projectsv2(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_projectsv2",
    description="Delete projectsV2 in GitHub"
)
def deletar_orgs_projectsv2(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_projects_columns",
    description="Modify columns in GitHub"
)
def modificar_projects_columns(column_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_columns_moves",
    description="Create moves in GitHub"
)
def criar_columns_moves(column_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_projects_collaborators",
    description="Delete collaborators in GitHub"
)
def deletar_projects_collaborators(project_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_projects_collaborators",
    description="Get collaborators in GitHub"
)
def obter_projects_collaborators(project_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_teams",
    description="Get teams in GitHub"
)
def obter_orgs_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_discussions",
    description="Get discussions in GitHub"
)
def obter_teams_discussions(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_security_advisories",
    description="Get security advisories in GitHub"
)
def obter_orgs_security_advisories(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_orgs_teams",
    description="Modify teams in GitHub"
)
def modificar_orgs_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_teams",
    description="Delete teams in GitHub"
)
def deletar_orgs_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_teams",
    description="Update teams in GitHub"
)
def atualizar_orgs_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_teams",
    description="Modify teams in GitHub"
)
def modificar_teams(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_teams_discussions",
    description="Modify discussions in GitHub"
)
def modificar_teams_discussions(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_teams_discussions",
    description="Delete discussions in GitHub"
)
def deletar_teams_discussions(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_invitations",
    description="Get invitations in GitHub"
)
def obter_teams_invitations(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_teams_members",
    description="Update members in GitHub"
)
def atualizar_teams_members(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_teams_members",
    description="Delete members in GitHub"
)
def deletar_teams_members(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_memberships",
    description="Get memberships in GitHub"
)
def obter_teams_memberships(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_teams_memberships",
    description="Update memberships in GitHub"
)
def atualizar_teams_memberships(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_teams_memberships",
    description="Delete memberships in GitHub"
)
def deletar_teams_memberships(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_repos",
    description="Get repos in GitHub"
)
def obter_teams_repos(team_id: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_teams_repos",
    description="Update repos in GitHub"
)
def atualizar_teams_repos(team_id: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_teams_repos",
    description="Delete repos in GitHub"
)
def deletar_teams_repos(team_id: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_teamsusers",
    description="Get teamsusers in GitHub"
)
def obter_teams_teamsusers(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_users",
    description="Get list of users in GitHub"
)
def listar_users() -> List[Dict[str, Any]]:
    url = "https://api.github.com/users"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_attestations_bulk_list",
    description="Create bulk list in GitHub"
)
def criar_attestations_bulk_list(username: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_users_attestations",
    description="Delete attestations in GitHub"
)
def deletar_users_attestations(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_attestations",
    description="Get attestations in GitHub"
)
def obter_users_attestations(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_gpg_keys",
    description="Get gpg keys in GitHub"
)
def obter_users_gpg_keys(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_cache_usage",
    description="Get usage in GitHub"
)
def obter_cache_usage(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_cache_usage_by_repository",
    description="Get usage by repository in GitHub"
)
def obter_cache_usage_by_repository(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_hosted_runners",
    description="Get hosted runners in GitHub"
)
def obter_actions_hosted_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_actions_hosted_runners",
    description="Create hosted runners in GitHub"
)
def criar_actions_hosted_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_images_partner",
    description="Get partner in GitHub"
)
def obter_images_partner(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_hosted_runners_limits",
    description="Get limits in GitHub"
)
def obter_hosted_runners_limits(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_hosted_runners_machine_sizes",
    description="Get machine sizes in GitHub"
)
def obter_hosted_runners_machine_sizes(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_hosted_runners_platforms",
    description="Get platforms in GitHub"
)
def obter_hosted_runners_platforms(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_customization_sub",
    description="Update sub in GitHub"
)
def atualizar_customization_sub(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_actions_permissions",
    description="Get permissions in GitHub"
)
def obter_actions_permissions(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_actions_permissions",
    description="Update permissions in GitHub"
)
def atualizar_actions_permissions(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_permissions_artifact_and_log_retention",
    description="Get artifact and log retention in GitHub"
)
def obter_permissions_artifact_and_log_retention(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_artifact_and_log_retention",
    description="Update artifact and log retention in GitHub"
)
def atualizar_permissions_artifact_and_log_retention(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_permissions_fork_pr_contributor_approval",
    description="Get fork pr contributor approval in GitHub"
)
def obter_permissions_fork_pr_contributor_approval(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_fork_pr_contributor_approval",
    description="Update fork pr contributor approval in GitHub"
)
def atualizar_permissions_fork_pr_contributor_approval(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_permissions_fork_pr_workflows_private_repos",
    description="Get fork pr workflows private repos in GitHub"
)
def obter_permissions_fork_pr_workflows_private_repos(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_fork_pr_workflows_private_repos",
    description="Update fork pr workflows private repos in GitHub"
)
def atualizar_permissions_fork_pr_workflows_private_repos(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_permissions_repositories",
    description="Get repositories in GitHub"
)
def obter_permissions_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_repositories",
    description="Update repositories in GitHub"
)
def atualizar_permissions_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_selected_actions",
    description="Update selected actions in GitHub"
)
def atualizar_permissions_selected_actions(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_permissions_self_hosted_runners",
    description="Get self hosted runners in GitHub"
)
def obter_permissions_self_hosted_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_self_hosted_runners",
    description="Update self hosted runners in GitHub"
)
def atualizar_permissions_self_hosted_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_self_hosted_runners_repositories",
    description="Get repositories in GitHub"
)
def obter_self_hosted_runners_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_self_hosted_runners_repositories",
    description="Update repositories in GitHub"
)
def atualizar_self_hosted_runners_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_workflow",
    description="Update workflow in GitHub"
)
def atualizar_permissions_workflow(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_actions_runner_groups",
    description="Create runner groups in GitHub"
)
def criar_actions_runner_groups(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_actions_runner_groups",
    description="Update runner groups in GitHub"
)
def atualizar_actions_runner_groups(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_runners_downloads",
    description="Get downloads in GitHub"
)
def obter_runners_downloads(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_runners_generate_jitconfig",
    description="Create generate jitconfig in GitHub"
)
def criar_runners_generate_jitconfig(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_runners_registration_token",
    description="Create registration token in GitHub"
)
def criar_runners_registration_token(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_runners_remove_token",
    description="Create remove token in GitHub"
)
def criar_runners_remove_token(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_actions_runners",
    description="Create runners in GitHub"
)
def criar_actions_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_actions_runners",
    description="Update runners in GitHub"
)
def atualizar_actions_runners(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_secrets_public_key",
    description="Get public key in GitHub"
)
def obter_secrets_public_key(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_actions_variables",
    description="Create variables in GitHub"
)
def criar_actions_variables(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_actions_variables",
    description="Update variables in GitHub"
)
def atualizar_actions_variables(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_feeds",
    description="Get list of feeds in GitHub"
)
def listar_feeds() -> List[Dict[str, Any]]:
    url = "https://api.github.com/feeds"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_networks",
    description="Get list of networks in GitHub"
)
def listar_networks() -> List[Dict[str, Any]]:
    url = "https://api.github.com/networks"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_events",
    description="Get events in GitHub"
)
def obter_orgs_events(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_events",
    description="Get events in GitHub"
)
def obter_users_events(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_events_public",
    description="Get public in GitHub"
)
def obter_events_public(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_received_events",
    description="Get received events in GitHub"
)
def obter_users_received_events(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_received_events_public",
    description="Get public in GitHub"
)
def obter_received_events_public(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_starred",
    description="Get starred in GitHub"
)
def obter_users_starred(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_subscriptions",
    description="Get subscriptions in GitHub"
)
def obter_users_subscriptions(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_apps",
    description="Get list of apps in GitHub"
)
def listar_apps() -> List[Dict[str, Any]]:
    url = "https://api.github.com/apps"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_installation_token",
    description="Delete list of token in GitHub"
)
def deletar_installation_token() -> Dict[str, Any]:
    url = "https://api.github.com/installation/token"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_budgets",
    description="Get budgets in GitHub"
)
def obter_billing_budgets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_usage",
    description="Get usage in GitHub"
)
def obter_billing_usage(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_usage_summary",
    description="Get summary in GitHub"
)
def obter_usage_summary(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_actions",
    description="Get actions in GitHub"
)
def obter_billing_actions(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_packages",
    description="Get packages in GitHub"
)
def obter_billing_packages(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_shared_storage",
    description="Get shared storage in GitHub"
)
def obter_billing_shared_storage(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_campaigns",
    description="Get campaigns in GitHub"
)
def obter_orgs_campaigns(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_campaigns",
    description="Create campaigns in GitHub"
)
def criar_orgs_campaigns(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_code_scanning_alerts",
    description="Get alerts in GitHub"
)
def obter_code_scanning_alerts(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_code_security_configurations",
    description="Get configurations in GitHub"
)
def obter_code_security_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_configurations_defaults",
    description="Get defaults in GitHub"
)
def obter_configurations_defaults(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_configurations_detach",
    description="Delete detach in GitHub"
)
def deletar_configurations_detach(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_code_security_configurations",
    description="Update configurations in GitHub"
)
def atualizar_code_security_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_codes_of_conduct",
    description="Get list of codes of conduct in GitHub"
)
def listar_codes_of_conduct() -> List[Dict[str, Any]]:
    url = "https://api.github.com/codes_of_conduct"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_codespaces",
    description="Get codespaces in GitHub"
)
def obter_orgs_codespaces(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_codespaces_access",
    description="Update access in GitHub"
)
def atualizar_codespaces_access(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_access_selected_users",
    description="Create selected users in GitHub"
)
def criar_access_selected_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_access_selected_users",
    description="Delete selected users in GitHub"
)
def deletar_access_selected_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_secrets_public_key_2",
    description="Get public key in GitHub"
)
def obter_secrets_public_key_2(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_copilot_billing",
    description="Get billing in GitHub"
)
def obter_copilot_billing(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_seats",
    description="Get seats in GitHub"
)
def obter_billing_seats(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_billing_selected_teams",
    description="Create selected teams in GitHub"
)
def criar_billing_selected_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_billing_selected_teams",
    description="Delete selected teams in GitHub"
)
def deletar_billing_selected_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_billing_selected_users",
    description="Create selected users in GitHub"
)
def criar_billing_selected_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_billing_selected_users",
    description="Delete selected users in GitHub"
)
def deletar_billing_selected_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_copilot_metrics",
    description="Get metrics in GitHub"
)
def obter_copilot_metrics(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_team",
    description="Get team in GitHub"
)
def obter_orgs_team(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_credentials_revoke",
    description="Create list of revoke in GitHub"
)
def criar_credentials_revoke() -> Dict[str, Any]:
    url = "https://api.github.com/credentials/revoke"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_dependabot_repository_access",
    description="Get repository access in GitHub"
)
def obter_dependabot_repository_access(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_dependabot_repository_access",
    description="Modify repository access in GitHub"
)
def modificar_dependabot_repository_access(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_repository_access_default_level",
    description="Update default level in GitHub"
)
def atualizar_repository_access_default_level(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_dependabot_alerts",
    description="Get alerts in GitHub"
)
def obter_dependabot_alerts(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_secrets_public_key_3",
    description="Get public key in GitHub"
)
def obter_secrets_public_key_3(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_emojis",
    description="Get list of emojis in GitHub"
)
def listar_emojis() -> List[Dict[str, Any]]:
    url = "https://api.github.com/emojis"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_gitignore_templates",
    description="Get list of templates in GitHub"
)
def listar_gitignore_templates() -> List[Dict[str, Any]]:
    url = "https://api.github.com/gitignore/templates"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_interaction_limits",
    description="Get interaction limits in GitHub"
)
def obter_orgs_interaction_limits(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_interaction_limits",
    description="Update interaction limits in GitHub"
)
def atualizar_orgs_interaction_limits(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_interaction_limits",
    description="Delete interaction limits in GitHub"
)
def deletar_orgs_interaction_limits(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_licenses",
    description="Get list of licenses in GitHub"
)
def listar_licenses() -> List[Dict[str, Any]]:
    url = "https://api.github.com/licenses"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_markdown",
    description="Create list of markdown in GitHub"
)
def criar_markdown() -> Dict[str, Any]:
    url = "https://api.github.com/markdown"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_markdown_raw",
    description="Create list of raw in GitHub"
)
def criar_markdown_raw() -> Dict[str, Any]:
    url = "https://api.github.com/markdown/raw"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_versions",
    description="Get list of versions in GitHub"
)
def listar_versions() -> List[Dict[str, Any]]:
    url = "https://api.github.com/versions"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_zen",
    description="Get list of zen in GitHub"
)
def listar_zen() -> List[Dict[str, Any]]:
    url = "https://api.github.com/zen"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_organizations",
    description="Get list of organizations in GitHub"
)
def listar_organizations() -> List[Dict[str, Any]]:
    url = "https://api.github.com/organizations"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_org_properties_values",
    description="Get values in GitHub"
)
def obter_org_properties_values(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_org_properties_values",
    description="Modify values in GitHub"
)
def modificar_org_properties_values(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_orgs",
    description="Get list of orgs in GitHub"
)
def listar_orgs() -> List[Dict[str, Any]]:
    url = "https://api.github.com/orgs"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_orgs_2",
    description="Modify list of orgs in GitHub"
)
def modificar_orgs_2() -> Dict[str, Any]:
    url = "https://api.github.com/orgs"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs",
    description="Delete list of orgs in GitHub"
)
def deletar_orgs() -> Dict[str, Any]:
    url = "https://api.github.com/orgs"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_artifacts",
    description="Get artifacts in GitHub"
)
def obter_orgs_artifacts(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_attestations_bulk_list_2",
    description="Create bulk list in GitHub"
)
def criar_attestations_bulk_list_2(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_attestations_delete_request",
    description="Create delete request in GitHub"
)
def criar_attestations_delete_request(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_attestations_digest",
    description="Delete digest in GitHub"
)
def deletar_attestations_digest(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_orgs_attestations",
    description="Delete attestations in GitHub"
)
def deletar_orgs_attestations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_api_route_stats",
    description="Get route stats in GitHub"
)
def obter_api_route_stats(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_summary_stats_users",
    description="Get users in GitHub"
)
def obter_summary_stats_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_time_stats_users",
    description="Get users in GitHub"
)
def obter_time_stats_users(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_invitations",
    description="Create invitations in GitHub"
)
def criar_orgs_invitations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_invitations",
    description="Delete invitations in GitHub"
)
def deletar_orgs_invitations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_issue_types",
    description="Get issue types in GitHub"
)
def obter_orgs_issue_types(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_issue_types",
    description="Create issue types in GitHub"
)
def criar_orgs_issue_types(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_issue_types",
    description="Update issue types in GitHub"
)
def atualizar_orgs_issue_types(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_orgs_outside_collaborators",
    description="Get outside collaborators in GitHub"
)
def obter_orgs_outside_collaborators(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_outside_collaborators",
    description="Update outside collaborators in GitHub"
)
def atualizar_orgs_outside_collaborators(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_orgs_personal_access_token_requests",
    description="Create personal access token requests in GitHub"
)
def criar_orgs_personal_access_token_requests(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_orgs_personal_access_tokens",
    description="Create personal access tokens in GitHub"
)
def criar_orgs_personal_access_tokens(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_properties_schema",
    description="Get schema in GitHub"
)
def obter_properties_schema(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_properties_schema",
    description="Modify schema in GitHub"
)
def modificar_properties_schema(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_properties_values",
    description="Modify values in GitHub"
)
def modificar_properties_values(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_orgs_public_members",
    description="Get public members in GitHub"
)
def obter_orgs_public_members(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_rulesets",
    description="Create rulesets in GitHub"
)
def criar_orgs_rulesets(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_rulesets_rule_suites",
    description="Get rule suites in GitHub"
)
def obter_rulesets_rule_suites(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_security_managers_teams",
    description="Update teams in GitHub"
)
def atualizar_security_managers_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_settings_immutable_releases",
    description="Update immutable releases in GitHub"
)
def atualizar_settings_immutable_releases(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_immutable_releases_repositories",
    description="Get repositories in GitHub"
)
def obter_immutable_releases_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_immutable_releases_repositories",
    description="Update repositories in GitHub"
)
def atualizar_immutable_releases_repositories(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_settings_network_configurations",
    description="Create network configurations in GitHub"
)
def criar_settings_network_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_users_orgs",
    description="Get orgs in GitHub"
)
def obter_users_orgs(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_docker_conflicts",
    description="Get conflicts in GitHub"
)
def obter_docker_conflicts(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_packages",
    description="Get packages in GitHub"
)
def obter_orgs_packages(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_packages",
    description="Get list of packages in GitHub"
)
def listar_user_packages() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/packages"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_docker_conflicts_2",
    description="Get conflicts in GitHub"
)
def obter_docker_conflicts_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_packages",
    description="Get packages in GitHub"
)
def obter_users_packages(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_private_registries",
    description="Get private registries in GitHub"
)
def obter_orgs_private_registries(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_private_registries",
    description="Create private registries in GitHub"
)
def criar_orgs_private_registries(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_private_registries_public_key",
    description="Get public key in GitHub"
)
def obter_private_registries_public_key(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_projects_columns",
    description="Get list of columns in GitHub"
)
def listar_projects_columns() -> List[Dict[str, Any]]:
    url = "https://api.github.com/projects/columns"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_projects_columns_2",
    description="Modify list of columns in GitHub"
)
def modificar_projects_columns_2() -> Dict[str, Any]:
    url = "https://api.github.com/projects/columns"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_projects_columns",
    description="Delete list of columns in GitHub"
)
def deletar_projects_columns() -> Dict[str, Any]:
    url = "https://api.github.com/projects/columns"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_projects_collaborators",
    description="Update collaborators in GitHub"
)
def atualizar_projects_collaborators(project_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_orgs_teams",
    description="Create teams in GitHub"
)
def criar_orgs_teams(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_teams_discussions",
    description="Create discussions in GitHub"
)
def criar_teams_discussions(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_orgs_repos",
    description="Get repos in GitHub"
)
def obter_orgs_repos(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_orgs_repos",
    description="Create repos in GitHub"
)
def criar_orgs_repos(org: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_repositories",
    description="Get list of repositories in GitHub"
)
def listar_repositories() -> List[Dict[str, Any]]:
    url = "https://api.github.com/repositories"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_repos",
    description="Get repos in GitHub"
)
def obter_users_repos(username: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/users/{username}/repos"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_search_code",
    description="Get list of code in GitHub"
)
def listar_search_code() -> List[Dict[str, Any]]:
    url = "https://api.github.com/search/code"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_search_commits",
    description="Get list of commits in GitHub"
)
def listar_search_commits() -> List[Dict[str, Any]]:
    url = "https://api.github.com/search/commits"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_search_issues",
    description="Get list of issues in GitHub"
)
def listar_search_issues() -> List[Dict[str, Any]]:
    url = "https://api.github.com/search/issues"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_search_labels",
    description="Get list of labels in GitHub"
)
def listar_search_labels() -> List[Dict[str, Any]]:
    url = "https://api.github.com/search/labels"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_search_repositories",
    description="Get list of repositories in GitHub"
)
def listar_search_repositories() -> List[Dict[str, Any]]:
    url = "https://api.github.com/search/repositories"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_search_topics",
    description="Get list of topics in GitHub"
)
def listar_search_topics() -> List[Dict[str, Any]]:
    url = "https://api.github.com/search/topics"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_search_users",
    description="Get list of users in GitHub"
)
def listar_search_users() -> List[Dict[str, Any]]:
    url = "https://api.github.com/search/users"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_secret_scanning_alerts",
    description="Get alerts in GitHub"
)
def obter_secret_scanning_alerts(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_secret_scanning_pattern_configurations",
    description="Get pattern configurations in GitHub"
)
def obter_secret_scanning_pattern_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_secret_scanning_pattern_configurations",
    description="Modify pattern configurations in GitHub"
)
def modificar_secret_scanning_pattern_configurations(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_advisories",
    description="Get list of advisories in GitHub"
)
def listar_advisories() -> List[Dict[str, Any]]:
    url = "https://api.github.com/advisories"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_teams",
    description="Get list of teams in GitHub"
)
def listar_teams() -> List[Dict[str, Any]]:
    url = "https://api.github.com/teams"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_teams_2",
    description="Modify list of teams in GitHub"
)
def modificar_teams_2() -> Dict[str, Any]:
    url = "https://api.github.com/teams"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_teams",
    description="Delete list of teams in GitHub"
)
def deletar_teams() -> Dict[str, Any]:
    url = "https://api.github.com/teams"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_members",
    description="Get members in GitHub"
)
def obter_teams_members(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_teams",
    description="Get teams in GitHub"
)
def obter_teams_teams(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user",
    description="Get list of user in GitHub"
)
def listar_user() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_attestations_delete_request_2",
    description="Create delete request in GitHub"
)
def criar_attestations_delete_request_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_attestations_digest_2",
    description="Delete digest in GitHub"
)
def deletar_attestations_digest_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_following",
    description="Get following in GitHub"
)
def obter_users_following(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_keys",
    description="Get keys in GitHub"
)
def obter_users_keys(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_social_accounts",
    description="Get social accounts in GitHub"
)
def obter_users_social_accounts(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_ssh_signing_keys",
    description="Get ssh signing keys in GitHub"
)
def obter_users_ssh_signing_keys(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_user_starred",
    description="Update list of starred in GitHub"
)
def atualizar_user_starred() -> Dict[str, Any]:
    url = "https://api.github.com/user/starred"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_starred",
    description="Delete list of starred in GitHub"
)
def deletar_user_starred() -> Dict[str, Any]:
    url = "https://api.github.com/user/starred"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_subscriptions",
    description="Get list of subscriptions in GitHub"
)
def listar_user_subscriptions() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/subscriptions"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_installations",
    description="Get list of installations in GitHub"
)
def listar_user_installations() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/installations"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_assignments_accepted_assignments",
    description="Get accepted assignments in GitHub"
)
def obter_assignments_accepted_assignments(assignment_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_classrooms_assignmentscode_scanning",
    description="Get assignmentscode scanning in GitHub"
)
def obter_classrooms_assignmentscode_scanning(classroom_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_codespaces_secrets_2",
    description="Update secrets in GitHub"
)
def atualizar_codespaces_secrets_2(secret_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_secrets_repositories",
    description="Get repositories in GitHub"
)
def obter_secrets_repositories(secret_name: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_secrets_repositories",
    description="Delete repositories in GitHub"
)
def deletar_secrets_repositories(secret_name: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_user_codespaces",
    description="Get codespaces in GitHub"
)
def obter_user_codespaces(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_user_codespaces",
    description="Delete codespaces in GitHub"
)
def deletar_user_codespaces(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_codespaces_machines",
    description="Get machines in GitHub"
)
def obter_codespaces_machines(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_repository_invitations",
    description="Get list of repository invitations in GitHub"
)
def listar_user_repository_invitations() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/repository_invitations"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_user_repository_invitations",
    description="Delete repository invitations in GitHub"
)
def deletar_user_repository_invitations(invitation_id: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_gists",
    description="Modify gists in GitHub"
)
def modificar_gists(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_gists_comments",
    description="Get comments in GitHub"
)
def obter_gists_comments(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_gists_comments",
    description="Modify comments in GitHub"
)
def modificar_gists_comments(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_gists_comments",
    description="Delete comments in GitHub"
)
def deletar_gists_comments(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_gists_commits",
    description="Get commits in GitHub"
)
def obter_gists_commits(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_gistsgit",
    description="Get gistsgit in GitHub"
)
def obter_users_gistsgit(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_public_members",
    description="Update public members in GitHub"
)
def atualizar_orgs_public_members(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_orgs_public_members",
    description="Delete public members in GitHub"
)
def deletar_orgs_public_members(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_memberships_orgs",
    description="Get list of orgs in GitHub"
)
def listar_memberships_orgs() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/memberships/orgs"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_memberships_orgs",
    description="Modify orgs in GitHub"
)
def modificar_memberships_orgs(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_docker_conflicts",
    description="Get list of conflicts in GitHub"
)
def listar_docker_conflicts() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/docker/conflicts"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_user_blocks",
    description="Update blocks in GitHub"
)
def atualizar_user_blocks(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_email_visibility",
    description="Modify list of visibility in GitHub"
)
def modificar_email_visibility() -> Dict[str, Any]:
    url = "https://api.github.com/user/email/visibility"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_user_following",
    description="Update following in GitHub"
)
def atualizar_user_following(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_user_gpg_keys",
    description="Get list of gpg keys in GitHub"
)
def listar_user_gpg_keys() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/gpg_keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_user_gpg_keys",
    description="Delete gpg keys in GitHub"
)
def deletar_user_gpg_keys(gpg_key_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_user_keys",
    description="Delete keys in GitHub"
)
def deletar_user_keys(key_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_user_ssh_signing_keys",
    description="Delete ssh signing keys in GitHub"
)
def deletar_user_ssh_signing_keys(ssh_signing_key_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_starred",
    description="Get list of starred in GitHub"
)
def listar_user_starred() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/starred"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_events_orgs",
    description="Get orgs in GitHub"
)
def obter_events_orgs(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_installations_repositories",
    description="Get repositories in GitHub"
)
def obter_installations_repositories(installation_id: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_marketplace_purchases",
    description="Get list of marketplace purchases in GitHub"
)
def listar_user_marketplace_purchases() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/marketplace_purchases"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_marketplace_purchases_stubbed",
    description="Get list of stubbed in GitHub"
)
def listar_marketplace_purchases_stubbed() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/marketplace_purchases/stubbed"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_actions_2",
    description="Get actions in GitHub"
)
def obter_billing_actions_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_packages_2",
    description="Get packages in GitHub"
)
def obter_billing_packages_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_premium_request_usage_2",
    description="Get usage in GitHub"
)
def obter_premium_request_usage_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_shared_storage_2",
    description="Get shared storage in GitHub"
)
def obter_billing_shared_storage_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_billing_usage_2",
    description="Get usage in GitHub"
)
def obter_billing_usage_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_usage_summary_2",
    description="Get summary in GitHub"
)
def obter_usage_summary_2(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_assignments",
    description="Get list of assignments in GitHub"
)
def listar_assignments() -> List[Dict[str, Any]]:
    url = "https://api.github.com/assignments"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_assignments_grades",
    description="Get grades in GitHub"
)
def obter_assignments_grades(assignment_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_classrooms",
    description="Get list of classrooms in GitHub"
)
def listar_classrooms() -> List[Dict[str, Any]]:
    url = "https://api.github.com/classrooms"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_classrooms_assignments",
    description="Get assignments in GitHub"
)
def obter_classrooms_assignments(classroom_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_codespaces",
    description="Get list of codespaces in GitHub"
)
def listar_user_codespaces() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/codespaces"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_codespaces",
    description="Create list of codespaces in GitHub"
)
def criar_user_codespaces() -> Dict[str, Any]:
    url = "https://api.github.com/user/codespaces"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_codespaces_secrets",
    description="Get list of secrets in GitHub"
)
def listar_codespaces_secrets() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/codespaces/secrets"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_secrets_public_key",
    description="Get list of public key in GitHub"
)
def listar_secrets_public_key() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/codespaces/secrets/public-key"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_codespaces_secrets_3",
    description="Update list of secrets in GitHub"
)
def atualizar_codespaces_secrets_3() -> Dict[str, Any]:
    url = "https://api.github.com/user/codespaces/secrets"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_codespaces_secrets_2",
    description="Delete list of secrets in GitHub"
)
def deletar_codespaces_secrets_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/codespaces/secrets"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_secrets_repositories",
    description="Update repositories in GitHub"
)
def atualizar_secrets_repositories(secret_name: str) -> List[Dict[str, Any]]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_user_codespaces",
    description="Modify list of codespaces in GitHub"
)
def modificar_user_codespaces() -> Dict[str, Any]:
    url = "https://api.github.com/user/codespaces"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_codespaces_2",
    description="Delete list of codespaces in GitHub"
)
def deletar_user_codespaces_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/codespaces"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_codespaces_exports",
    description="Create exports in GitHub"
)
def criar_codespaces_exports(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_codespaces_exports",
    description="Get exports in GitHub"
)
def obter_codespaces_exports(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_codespaces_publish",
    description="Create publish in GitHub"
)
def criar_codespaces_publish(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_codespaces_start",
    description="Create start in GitHub"
)
def criar_codespaces_start(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_codespaces_stop",
    description="Create stop in GitHub"
)
def criar_codespaces_stop(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="modificar_user_repository_invitations",
    description="Modify list of repository invitations in GitHub"
)
def modificar_user_repository_invitations() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/repository_invitations"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_repository_invitations_2",
    description="Delete list of repository invitations in GitHub"
)
def deletar_user_repository_invitations_2() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/repository_invitations"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_gists",
    description="Get list of gists in GitHub"
)
def listar_gists() -> List[Dict[str, Any]]:
    url = "https://api.github.com/gists"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_gists",
    description="Create list of gists in GitHub"
)
def criar_gists() -> Dict[str, Any]:
    url = "https://api.github.com/gists"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_gists_public",
    description="Get list of public in GitHub"
)
def listar_gists_public() -> List[Dict[str, Any]]:
    url = "https://api.github.com/gists/public"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_gists_starred",
    description="Get list of starred in GitHub"
)
def listar_gists_starred() -> List[Dict[str, Any]]:
    url = "https://api.github.com/gists/starred"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_gists_2",
    description="Modify list of gists in GitHub"
)
def modificar_gists_2() -> Dict[str, Any]:
    url = "https://api.github.com/gists"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_gists",
    description="Delete list of gists in GitHub"
)
def deletar_gists() -> Dict[str, Any]:
    url = "https://api.github.com/gists"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_gists_comments",
    description="Create comments in GitHub"
)
def criar_gists_comments(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_gists_forks",
    description="Get forks in GitHub"
)
def obter_gists_forks(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_gists_forks",
    description="Create forks in GitHub"
)
def criar_gists_forks(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_gists_star",
    description="Get star in GitHub"
)
def obter_gists_star(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_gists_star",
    description="Update star in GitHub"
)
def atualizar_gists_star(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_gists_star",
    description="Delete star in GitHub"
)
def deletar_gists_star(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_gists",
    description="Get gists in GitHub"
)
def obter_users_gists(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_interaction_limits",
    description="Get list of interaction limits in GitHub"
)
def listar_user_interaction_limits() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/interaction-limits"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_user_interaction_limits",
    description="Update list of interaction limits in GitHub"
)
def atualizar_user_interaction_limits() -> Dict[str, Any]:
    url = "https://api.github.com/user/interaction-limits"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_interaction_limits",
    description="Delete list of interaction limits in GitHub"
)
def deletar_user_interaction_limits() -> Dict[str, Any]:
    url = "https://api.github.com/user/interaction-limits"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_issues",
    description="Get list of issues in GitHub"
)
def listar_issues() -> List[Dict[str, Any]]:
    url = "https://api.github.com/issues"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_issues",
    description="Get issues in GitHub"
)
def obter_orgs_issues(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_issues",
    description="Get list of issues in GitHub"
)
def listar_user_issues() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/issues"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_memberships_orgs_2",
    description="Modify list of orgs in GitHub"
)
def modificar_memberships_orgs_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/memberships/orgs"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_user_orgs",
    description="Get list of orgs in GitHub"
)
def listar_user_orgs() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/orgs"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_repos",
    description="Get list of repos in GitHub"
)
def listar_user_repos() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/repos"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_repos",
    description="Create list of repos in GitHub"
)
def criar_user_repos() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/repos"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_user_teams",
    description="Get list of teams in GitHub"
)
def listar_user_teams() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/teams"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_user",
    description="Modify list of user in GitHub"
)
def modificar_user() -> Dict[str, Any]:
    url = "https://api.github.com/user"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_user_blocks",
    description="Get list of blocks in GitHub"
)
def listar_user_blocks() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/blocks"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_user_blocks_2",
    description="Update list of blocks in GitHub"
)
def atualizar_user_blocks_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/blocks"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_blocks",
    description="Delete list of blocks in GitHub"
)
def deletar_user_blocks() -> Dict[str, Any]:
    url = "https://api.github.com/user/blocks"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_emails",
    description="Get list of emails in GitHub"
)
def listar_user_emails() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/emails"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_emails",
    description="Create list of emails in GitHub"
)
def criar_user_emails() -> Dict[str, Any]:
    url = "https://api.github.com/user/emails"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_emails",
    description="Delete list of emails in GitHub"
)
def deletar_user_emails() -> Dict[str, Any]:
    url = "https://api.github.com/user/emails"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_following",
    description="Get list of following in GitHub"
)
def listar_user_following() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/following"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_user_following_2",
    description="Update list of following in GitHub"
)
def atualizar_user_following_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/following"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_following",
    description="Delete list of following in GitHub"
)
def deletar_user_following() -> Dict[str, Any]:
    url = "https://api.github.com/user/following"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_gpg_keys",
    description="Create list of gpg keys in GitHub"
)
def criar_user_gpg_keys() -> Dict[str, Any]:
    url = "https://api.github.com/user/gpg_keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_gpg_keys_2",
    description="Delete list of gpg keys in GitHub"
)
def deletar_user_gpg_keys_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/gpg_keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_keys",
    description="Get list of keys in GitHub"
)
def listar_user_keys() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_keys",
    description="Create list of keys in GitHub"
)
def criar_user_keys() -> Dict[str, Any]:
    url = "https://api.github.com/user/keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_keys_2",
    description="Delete list of keys in GitHub"
)
def deletar_user_keys_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_public_emails",
    description="Get list of public emails in GitHub"
)
def listar_user_public_emails() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/public_emails"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_social_accounts",
    description="Get list of social accounts in GitHub"
)
def listar_user_social_accounts() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/social_accounts"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_social_accounts",
    description="Create list of social accounts in GitHub"
)
def criar_user_social_accounts() -> Dict[str, Any]:
    url = "https://api.github.com/user/social_accounts"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_social_accounts",
    description="Delete list of social accounts in GitHub"
)
def deletar_user_social_accounts() -> Dict[str, Any]:
    url = "https://api.github.com/user/social_accounts"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_ssh_signing_keys",
    description="Get list of ssh signing keys in GitHub"
)
def listar_user_ssh_signing_keys() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/ssh_signing_keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_ssh_signing_keys",
    description="Create list of ssh signing keys in GitHub"
)
def criar_user_ssh_signing_keys() -> Dict[str, Any]:
    url = "https://api.github.com/user/ssh_signing_keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_user_ssh_signing_keys_2",
    description="Delete list of ssh signing keys in GitHub"
)
def deletar_user_ssh_signing_keys_2() -> Dict[str, Any]:
    url = "https://api.github.com/user/ssh_signing_keys"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_gists_2",
    description="Delete gists in GitHub"
)
def deletar_gists_2(gist_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_orgs_2",
    description="Delete orgs in GitHub"
)
def deletar_orgs_2(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_memberships_orgs",
    description="Get orgs in GitHub"
)
def obter_memberships_orgs(org: str, page: int = 1) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    params['page'] = page
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_keyshelp",
    description="Get keysHelp in GitHub"
)
def obter_users_keyshelp(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_selected_actionswriteuatiat",
    description="Update selected actionswriteUATIAT in GitHub"
)
def atualizar_permissions_selected_actionswriteuatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_workflowwriteuatiat",
    description="Update workflowwriteUATIAT in GitHub"
)
def atualizar_permissions_workflowwriteuatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_billing_selected_teamswriteuatiatmultiple",
    description="Delete selected teamswriteUATIATMultiple in GitHub"
)
def deletar_billing_selected_teamswriteuatiatmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_billing_selected_userswriteuatiatmultiple",
    description="Create selected userswriteUATIATMultiple in GitHub"
)
def criar_billing_selected_userswriteuatiatmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_billing_selected_userswriteuatiatmultiple",
    description="Delete selected userswriteUATIATMultiple in GitHub"
)
def deletar_billing_selected_userswriteuatiatmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_interaction_limitswriteuatiat",
    description="Update interaction limitswriteUATIAT in GitHub"
)
def atualizar_orgs_interaction_limitswriteuatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_billing_seatsreaduatiatmultiple",
    description="Get seatsreadUATIATMultiple in GitHub"
)
def obter_billing_seatsreaduatiatmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_copilot_metricsreaduatiatmultiple",
    description="Get metricsreadUATIATMultiple in GitHub"
)
def obter_copilot_metricsreaduatiatmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_installationsreaduatiat",
    description="Get installationsreadUATIAT in GitHub"
)
def obter_orgs_installationsreaduatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_secret_scanning_pattern_configurationsreaduatiat",
    description="Get pattern configurationsreadUATIAT in GitHub"
)
def obter_secret_scanning_pattern_configurationsreaduatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_copilot_billingreaduatiatmultiple",
    description="Get billingreadUATIATMultiple in GitHub"
)
def obter_copilot_billingreaduatiatmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_teamsreaduatiat",
    description="Get teamsreadUATIAT in GitHub"
)
def obter_teams_teamsreaduatiat(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_codespaces_secretsreaduatiat",
    description="Get secretsreadUATIAT in GitHub"
)
def obter_codespaces_secretsreaduatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_codespacesreaduatiatmultiple",
    description="Get codespacesreadUATIATMultiple in GitHub"
)
def obter_orgs_codespacesreaduatiatmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_dependabot_secretsreaduatiat",
    description="Get secretsreadUATIAT in GitHub"
)
def obter_dependabot_secretsreaduatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_projects_collaboratorsadminuatiatmultiple",
    description="Get collaboratorsadminUATIATMultiple in GitHub"
)
def obter_projects_collaboratorsadminuatiatmultiple(project_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_projects_columns_2",
    description="Delete columns in GitHub"
)
def deletar_projects_columns_2(column_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_columns_moveswriteuatiatmultiple",
    description="Create moveswriteUATIATMultiple in GitHub"
)
def criar_columns_moveswriteuatiatmultiple(column_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_orgs_projectsv2readuatiat",
    description="Get projectsV2readUATIAT in GitHub"
)
def obter_orgs_projectsv2readuatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_secretsreaduatiat",
    description="Get secretsreadUATIAT in GitHub"
)
def obter_actions_secretsreaduatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_variablesreaduatiat",
    description="Get variablesreadUATIAT in GitHub"
)
def obter_actions_variablesreaduatiat(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_reposwriteuat",
    description="Create list of reposwriteUAT in GitHub"
)
def criar_user_reposwriteuat() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/reposwriteUAT"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_codespaces_exportswriteuat",
    description="Create exportswriteUAT in GitHub"
)
def criar_codespaces_exportswriteuat(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_projects_collaboratorswriteuatiatmultiple",
    description="Get collaboratorswriteUATIATMultiple in GitHub"
)
def obter_projects_collaboratorswriteuatiatmultiple(project_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_projects_columns",
    description="Get columns in GitHub"
)
def obter_projects_columns(column_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_codespaces_secretsreaduat",
    description="Get list of secretsreadUAT in GitHub"
)
def listar_codespaces_secretsreaduat() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/codespaces/secretsreadUAT"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_starredreaduat",
    description="Get list of starredreadUAT in GitHub"
)
def listar_user_starredreaduat() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/starredreadUAT"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_starredreaduatiatuser",
    description="Get starredreadUATIATUser in GitHub"
)
def obter_users_starredreaduatiatuser(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_starredreaduatiat",
    description="Get starredreadUATIAT in GitHub"
)
def obter_users_starredreaduatiat(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_selected_actionswrite",
    description="Update selected actionswrite in GitHub"
)
def atualizar_permissions_selected_actionswrite(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="atualizar_permissions_workflowwrite",
    description="Update workflowwrite in GitHub"
)
def atualizar_permissions_workflowwrite(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_billing_selected_teamswritemultiple",
    description="Delete selected teamswriteMultiple in GitHub"
)
def deletar_billing_selected_teamswritemultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_billing_selected_userswritemultiple",
    description="Create selected userswriteMultiple in GitHub"
)
def criar_billing_selected_userswritemultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_billing_selected_userswritemultiple",
    description="Delete selected userswriteMultiple in GitHub"
)
def deletar_billing_selected_userswritemultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_orgs_interaction_limitswrite",
    description="Update interaction limitswrite in GitHub"
)
def atualizar_orgs_interaction_limitswrite(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_billing_seatsreadmultiple",
    description="Get seatsreadMultiple in GitHub"
)
def obter_billing_seatsreadmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_copilot_metricsreadmultiple",
    description="Get metricsreadMultiple in GitHub"
)
def obter_copilot_metricsreadmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_installationsread",
    description="Get installationsread in GitHub"
)
def obter_orgs_installationsread(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_secret_scanning_pattern_configurationsread",
    description="Get pattern configurationsread in GitHub"
)
def obter_secret_scanning_pattern_configurationsread(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_copilot_billingreadmultiple",
    description="Get billingreadMultiple in GitHub"
)
def obter_copilot_billingreadmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_teams_teamsread",
    description="Get teamsread in GitHub"
)
def obter_teams_teamsread(team_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_codespaces_secretsread",
    description="Get secretsread in GitHub"
)
def obter_codespaces_secretsread(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_codespacesreadmultiple",
    description="Get codespacesreadMultiple in GitHub"
)
def obter_orgs_codespacesreadmultiple(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_dependabot_secretsread",
    description="Get secretsread in GitHub"
)
def obter_dependabot_secretsread(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_projects_collaboratorsadminmultiple",
    description="Get collaboratorsadminMultiple in GitHub"
)
def obter_projects_collaboratorsadminmultiple(project_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_projects_columns_3",
    description="Delete columns in GitHub"
)
def deletar_projects_columns_3(column_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_columns_moveswritemultiple",
    description="Create moveswriteMultiple in GitHub"
)
def criar_columns_moveswritemultiple(column_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="obter_orgs_projectsv2read",
    description="Get projectsV2read in GitHub"
)
def obter_orgs_projectsv2read(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_secretsread",
    description="Get secretsread in GitHub"
)
def obter_actions_secretsread(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_actions_variablesread",
    description="Get variablesread in GitHub"
)
def obter_actions_variablesread(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_user_reposwrite",
    description="Create list of reposwrite in GitHub"
)
def criar_user_reposwrite() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/reposwrite"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_codespaces_exportswrite",
    description="Create exportswrite in GitHub"
)
def criar_codespaces_exportswrite(codespace_name: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_codespaces_secretsread",
    description="Get list of secretsread in GitHub"
)
def listar_codespaces_secretsread() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/codespaces/secretsread"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_user_starredread",
    description="Get list of starredread in GitHub"
)
def listar_user_starredread() -> List[Dict[str, Any]]:
    url = "https://api.github.com/user/starredread"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_starredreaduser",
    description="Get starredreadUser in GitHub"
)
def obter_users_starredreaduser(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_starredread",
    description="Get starredread in GitHub"
)
def obter_users_starredread(username: str) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_users_installation",
    description="Get installation in GitHub"
)
def obter_users_installation(username: str, page: int = 1) -> Dict[str, Any]:
    url = "https://api.github.com//{username}"
    headers = get_headers()
    params = {}
    payload = {}
    url = url.format(username=username)
    params['page'] = page
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_orgs_installation",
    description="Get installation in GitHub"
)
def obter_orgs_installation(org: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="criar_app_manifests_conversions",
    description="Create conversions in GitHub"
)
def criar_app_manifests_conversions(code: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="listar_images_github_owned",
    description="Get list of github owned in GitHub"
)
def listar_images_github_owned() -> List[Dict[str, Any]]:
    url = "https://api.github.com/actions/hosted-runners/images/github-owned"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_images_partner",
    description="Get list of partner in GitHub"
)
def listar_images_partner() -> List[Dict[str, Any]]:
    url = "https://api.github.com/actions/hosted-runners/images/partner"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="listar_notifications",
    description="Get list of notifications in GitHub"
)
def listar_notifications() -> List[Dict[str, Any]]:
    url = "https://api.github.com/notifications"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="obter_organizations_team",
    description="Get team in GitHub"
)
def obter_organizations_team(org_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="modificar_organizations_team",
    description="Modify team in GitHub"
)
def modificar_organizations_team(org_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_organizations_team",
    description="Delete team in GitHub"
)
def deletar_organizations_team(org_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="atualizar_organizations_team",
    description="Update team in GitHub"
)
def atualizar_organizations_team(org_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_organizations_team",
    description="Create team in GitHub"
)
def criar_organizations_team(org_id: str) -> Dict[str, Any]:
    url = "https://api.github.com/"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="criar_organizations",
    description="Create list of organizations in GitHub"
)
def criar_organizations() -> Dict[str, Any]:
    url = "https://api.github.com/organizations"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Repositório ou recurso não encontrado.")
        if status == 403:
            raise ToolError("Sem permissão para esta ação.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro: {str(e)}")


@mcp.tool(
    name="deletar_organizations",
    description="Delete list of organizations in GitHub"
)
def deletar_organizations() -> Dict[str, Any]:
    url = "https://api.github.com/organizations"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")


@mcp.tool(
    name="deletar_repositories",
    description="Delete list of repositories in GitHub"
)
def deletar_repositories() -> List[Dict[str, Any]]:
    url = "https://api.github.com/repositories"
    headers = get_headers()
    params = {}
    payload = {}
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return [
                    {k: item.get(k) for k in ["login", "id", "html_url", "name", "full_name"] if k in item}
                    for item in data
                ]
            return data
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            raise ToolError("Recurso não encontrado.")
        if status == 403:
            raise ToolError("Token inválido ou sem permissão.")
        raise ToolError(f"Erro {status}: {e.response.text[:200]}")
    except Exception as e:
        raise ToolError(f"Erro inesperado: {str(e)}")



if __name__ == "__main__":
    mcp.run()