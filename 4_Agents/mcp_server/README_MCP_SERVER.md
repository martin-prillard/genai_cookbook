# MCP Server for Cursor

This directory contains an example MCP (Model Context Protocol) server that can be used with Cursor IDE.

## Files

- `mcp_server_example.py`: The MCP server implementation

## Quick Start

1. **Install the MCP SDK**:
   ```bash
   pip install mcp
   ```

2. **Configure Cursor**:
   - The following json can be created manually and added to any client:
     ```json
     {
       "mcpServers": {
         "example-mcp-server": {
           "command": "python",
           "args": ["/absolute/path/to/4_Agents/mcp_server.py"]
         }
       }
     }
     ```

3. **Restart Cursor** to load the server

4. **Verify Connection**:
   - Go to Settings → Features → MCP
   - You should see "example-mcp-server" listed

## Available Tools

The server provides four tools:

1. **calculate**: Perform basic math operations (add, subtract, multiply, divide)
2. **read_file**: Read text files from the project directory
3. **list_files**: List files and directories
4. **get_project_info**: Get Python project information

## Usage in Cursor

Once connected, you can use the tools in Cursor's chat:

- "Calculate 15 * 23"
- "List files in the 4_Agents directory"
- "Read the README.md file"
- "Get project information"

## Testing

Test the server independently using MCP Inspector:

```bash
npx @modelcontextprotocol/inspector python mcp_server_example.py
```

## Security

The server includes security measures:
- File access restricted to project directory
- Path traversal protection
- Input validation

## Customization

See the notebook for instructions on adding new tools to the server.



