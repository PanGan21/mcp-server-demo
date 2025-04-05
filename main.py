from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import json
import os
import httpx

load_dotenv()

mcp = FastMCP("documentation")

USER_AGENT = "dockes-app/1.0"
SERVER_URL = "https://google.serper.dev/search"

docs_url = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs"
}


async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q": query, "num": 2})

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(SERVER_URL, headers=headers, data=payload, timeout=30.0)
            response.raise_for_status()
            return response.json
        except httpx.TimeoutException:
            return {"organic": []}


def fetch_url():
    pass


def get_docs():
    pass


def main():
    print("Setup")


if __name__ == "__main__":
    main()
