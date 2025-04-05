from dotenv import load_dotenv
import json
import os
import httpx
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

from src.constants import SERPER_URL, docs_urls

load_dotenv()


async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q": query, "num": 2})

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(SERPER_URL, headers=headers, data=payload, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}


async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout error"


def register_tools(mcp: FastMCP):
    """Register all tools with the MCP server"""

    @mcp.tool()
    async def get_docs(query: str, library: str):
        """
        Search the latest docs for a given query and library.
        Supports langchain, openai and llama-index.

        Args:
          query: The query to search for (e.g. "Chroma DB")
          library: The library to search in (e.g. "langchain")

        Returns:
          Text from the docs
        """
        if library not in docs_urls:
            raise ValueError(f"Library {library} not supported by this tool")

        query = f"site:{docs_urls[library]} {query}"
        results = await search_web(query)
        if len(results["organic"]) == 0:
            return "No results found"

        text = ""
        for result in results["organic"]:
            text += await fetch_url(result["link"])

        return text
