from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("Python MCP Server Demo")


@mcp.tool()
async def fetch_cep(cep: str) -> dict:
    """
    Fetches data for a specified CEP.
    CEP is a 8-digit code used in Brazil to identify addresses.
    
    Args:
        cep (str): The CEP to fetch data for.
        
    Returns:
        dict: The CEP data.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")
        return response.json()