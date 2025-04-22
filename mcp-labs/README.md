# MCP Labs - Multiple Completion Providers

This repository contains examples of Model Context Protocol (MCP) server implementations in different programming languages. Each implementation demonstrates how to create an MCP server that provides a tool for fetching Brazilian postal code (CEP) data.

## Overview

MCP (Model Context Protocol) is a protocol that enables AI models to interact with external tools and services. This repository demonstrates how to implement MCP servers in:

- Python : `python` folder
- Java : `java` folder
- C# : `csharp` folder

Each implementation provides the same functionality: a tool called `fetch_cep` that retrieves information about a Brazilian postal code (CEP).

## Example of MCP Server in Action

- What is the name of the city with CEP 89900000?
- Give me the address of CEP 89909000 and open in a map

## Configuration

Change the path to match your local setup.

Use just one server at a time.

### Python

```json
{
  "mcpServers": {
    "Python MCP Server Demo": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/johnimarangon/Projects/youtube-videos-code-examples/mcp-labs/python/server.py"
      ]
    }
  }
}
```

### Java

```json
{
  "mcpServers": {
    "Java MCP Server Demo": {
      "command": "java",
      "args": [
        "-jar",
        "/Users/johnimarangon/Projects/youtube-videos-code-examples/MCP-Labs/java/target/mcp-demo-1.0-SNAPSHOT.jar"
      ]
    }
  }
}
```

### C#

```json
{
  "mcpServers": {
    "C# MCP Server Demo": {
      "command": "dotnet",
      "args": [
        "run",
        "--project",
        "/Users/johnimarangon/Projects/youtube-videos-code-examples/mcp-labs/csharp/csharp.csproj"
      ]
    }
  }
}
```

## Integration with AI Models

These MCP servers can be integrated with AI models that support the Model Context Protocol. The servers communicate through standard input/output, making them easy to integrate with various AI systems.

## Inspect Tool

- https://github.com/modelcontextprotocol/inspector  

### Python

```bash
npx @modelcontextprotocol/inspector uv run --with mcp mcp run server.py
```

### Java

```bash
npx @modelcontextprotocol/inspector java -jar java/target/mcp-demo-1.0-SNAPSHOT.jar
```

### C#

```bash
npx @modelcontextprotocol/inspector dotnet run --project csharp/csharp.csproj --no-build
```
