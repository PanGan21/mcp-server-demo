from mcp.server.fastmcp import FastMCP
from src.tools import register_tools


def create_app() -> FastMCP:
    """Create and configure the MCP server"""
    mcp = FastMCP("documentation")
    register_tools(mcp)
    return mcp


if __name__ == "__main__":
    app = create_app()
    app.run(transport="stdio")
