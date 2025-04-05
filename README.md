# mc-server-demo

A Model Context Protocol (MCP) server implementation that can retieve the latest documentation of a queried library.

## Setup locally

- The MCP tool is using [Serper API](https://serper.dev/) to seach or Google therefore an api key should be specified. See [.env.example](.env.example) on how to define it.
- Create a virtual environment: `python -m venv .venv`
- Activate the virtual environemt: `source .venv/bin/activate`
- Install the required dependencies: `pip install -r requirements.txt`

## Debug

- Run usin Model Context Protocol inspector.
- Visit the local inspector url displayed on terminal.
- List the available tools and use `get_docs` to input queries.

## Client integration

- Example of Cursor IDE
- Navigate to AI settings
- Under "Custom MCP Server", add the following configuration:
  ```json
  {
    "command": "${workspaceFolder}/.venv/bin/python",
    "args": ["main.py"]
  }
  ```
