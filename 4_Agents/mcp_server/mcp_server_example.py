#!/usr/bin/env python3
"""
MCP Server Example - A simple MCP server using the official Python SDK

This server provides example tools that can be used by Cursor or other MCP clients.
"""

import asyncio
import sys
from typing import Any, Awaitable, Callable, Sequence
from pathlib import Path

# Try to import the official MCP SDK
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
    MCP_SDK_AVAILABLE = True
except ImportError:
    # Fallback if SDK not available - we'll handle this in the notebook
    MCP_SDK_AVAILABLE = False
    print("Warning: Official MCP SDK not installed. Install with: pip install mcp")


# Create the MCP server instance
if MCP_SDK_AVAILABLE:
    app = Server("example-mcp-server")
else:
    app = None


# Helper functions (available regardless of MCP SDK)
def get_project_root() -> Path:
    """Get the project root directory (parent of the directory containing this file)."""
    return Path(__file__).parent.parent


def validate_path_within_project(path: Path, project_root: Path) -> bool:
    """Validate that a path is within the project root directory."""
    return str(path.resolve()).startswith(str(project_root.resolve()))


# Define tools and handlers (only when MCP SDK is available)
if MCP_SDK_AVAILABLE:
    # Tool handler functions
    async def handle_calculate(arguments: dict[str, Any]) -> Sequence[TextContent]:
        """Handle the calculate tool - perform mathematical operations."""
        operation = arguments.get("operation")
        a = arguments.get("a")
        b = arguments.get("b")
        
        if operation == "add":
            #! to complete
            result = ...
        elif operation == "subtract":
            result = ...
            #! to complete
        elif operation == "multiply":
            result = ...
            #! to complete
        elif operation == "divide":
            #! to complete
            result = ...
        else:
            return [TextContent(type="text", text=f"Error: Unknown operation {operation}")]
        
        return ... #! to complete


    async def handle_read_file(arguments: dict[str, Any]) -> Sequence[TextContent]:
        """Handle the read_file tool - read a file from the project directory."""
        filepath = arguments.get("filepath")
        try:
            # Security: Only allow reading from project directory
            project_root = get_project_root()
            full_path = (project_root / filepath).resolve()
            
            # Ensure the path is within project root
            if not validate_path_within_project(full_path, project_root):
                return [TextContent(type="text", text=f"Error: Access denied. File outside project directory.")]
            
            if not full_path.exists():
                return [TextContent(type="text", text=f"Error: File not found: {filepath}")]
            
            content = full_path.read_text(encoding="utf-8")
            return [TextContent(type="text", text=f"File contents of {filepath}:\n\n{content}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error reading file: {str(e)}")]


    async def handle_list_files(arguments: dict[str, Any]) -> Sequence[TextContent]:
        """Handle the list_files tool - list files in a directory."""
        directory = arguments.get("directory", ".")
        try:
            project_root = get_project_root()
            dir_path = (project_root / directory).resolve()
            
            # Ensure the path is within project root
            if not validate_path_within_project(dir_path, project_root):
                return [TextContent(type="text", text=f"Error: Access denied. Directory outside project directory.")]
            
            if not dir_path.exists():
                return [TextContent(type="text", text=f"Error: Directory not found: {directory}")]
            
            if not dir_path.is_dir():
                return [TextContent(type="text", text=f"Error: Path is not a directory: {directory}")]
            
            files = [f.name for f in dir_path.iterdir() if f.is_file()]
            dirs = [d.name for d in dir_path.iterdir() if d.is_dir()]
            
            result = f"Files in {directory}:\n"
            if files:
                result += "\nFiles:\n" + "\n".join(f"  - {f}" for f in sorted(files))
            if dirs:
                result += "\nDirectories:\n" + "\n".join(f"  - {d}/" for d in sorted(dirs))
            if not files and not dirs:
                result += "  (empty)"
            
            return [TextContent(type="text", text=result)]
        except Exception as e:
            return [TextContent(type="text", text=f"Error listing files: {str(e)}")]


    async def handle_get_project_info(arguments: dict[str, Any]) -> Sequence[TextContent]:
        """Handle the get_project_info tool - get information about the project."""
        try:
            project_root = get_project_root()
            info = []
            
            # Check for Python version
            info.append(f"Python version: {sys.version}")
            
            # Check for requirements.txt
            req_file = project_root / "requirements.txt"
            if req_file.exists():
                info.append(f"\nDependencies (from requirements.txt):")
                deps = req_file.read_text(encoding="utf-8").strip().split("\n")
                info.extend([f"  - {dep}" for dep in deps if dep.strip()])
            
            # Check for pyproject.toml
            pyproject_file = project_root / "pyproject.toml"
            if pyproject_file.exists():
                info.append(f"\nProject configuration found: pyproject.toml")
            
            return [TextContent(type="text", text="\n".join(info))]
        except Exception as e:
            return [TextContent(type="text", text=f"Error getting project info: {str(e)}")]

    #! TODO: add a tool to get the list of students in this class right now

    # Tool handler registry - maps tool names to their handler functions
    # Each handler is an async function that takes arguments and returns TextContent
    TOOL_HANDLERS: dict[str, Callable[[dict[str, Any]], Awaitable[Sequence[TextContent]]]] = {
        "calculate": handle_calculate,
        "read_file": handle_read_file,
        "list_files": handle_list_files,
        "get_project_info": handle_get_project_info,
    }

    # Define tools
    @app.list_tools()
    async def list_tools() -> list[Tool]:
        """List all available tools in this MCP server."""
        return [
            Tool(
                name="calculate",
                description="Perform basic mathematical calculations (add, subtract, multiply, divide)",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "operation": {
                            "type": "string",
                            "enum": ["add", "subtract", "multiply", "divide"],
                            "description": "The mathematical operation to perform"
                        },
                        "a": {
                            "type": "number",
                            "description": "First number"
                        },
                        "b": { #! to complete
                        }
                    },
                    "required": ["operation", "a", "b"]
                }
            ),
            Tool(
                name="read_file",
                description="Read the contents of a text file from the project directory",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "filepath": {
                            "type": "string",
                            "description": "Path to the file relative to the project root"
                        }
                    },
                    "required": [""] #! to complete
                }
            ),
            Tool(
                name="list_files",
                description="List all files in a directory",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "directory": {
                            "type": "string",
                            "description": "Directory path relative to project root (default: current directory)",
                            "default": "."
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="get_project_info",
                description="Get information about the current project (Python version, dependencies, etc.)",
                inputSchema={
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            )
        ]

    @app.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
        """Handle tool calls from the MCP client and route to appropriate handler."""
        # Look up the handler in the registry
        handler = TOOL_HANDLERS.get(name)
        if handler:
            #! to complete
            return ...
        else:
            return [TextContent(type="text", text=f"Error: Unknown tool '{name}'")]


async def main():
    """Main entry point for the MCP server."""
    if not MCP_SDK_AVAILABLE:
        print("Error: MCP SDK not available. Please install it with: pip install mcp", file=sys.stderr)
        sys.exit(1)
    
    # Run the server using stdio transport
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())



