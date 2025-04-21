
# MCP Server written in C#

##### Running the project:

```
dotnet run
```

```
dotnet build csharp.csproj -c Release
```

##### Inspect

```
npx @modelcontextprotocol/inspector dotnet run --project csharp.csproj --no-build
```

##### Add to Claude's config:

```json
{
  "mcpServers": {
    "csharp-mcp": {
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
