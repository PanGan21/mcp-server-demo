from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("documentation")

USER_AGENT = "dockes-app/1.0"
SERVER_URL = "https://google.serper.dev/search"

docs_url = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs"
}


def search_web():
    pass


def fetch_url():
    pass


@mcp.tool
def get_docs():
    pass


def main():
    print("Setup")


if __name__ == "__main__":
    main()
