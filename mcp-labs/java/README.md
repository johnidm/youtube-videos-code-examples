# MCP Server written in Java


##### Running the project:

```
mvn clean package
```

```
java -jar target/mcp-demo-1.0-SNAPSHOT.jar
```

##### Inspect the project:

```
npx @modelcontextprotocol/inspector java -jar target/mcp-demo-1.0-SNAPSHOT.jar
```

##### Add to Claude's config:

```
{
  "java-mcp": {
    "command": "java",
    "args": [
      "-jar",
      "/Users/johnimarangon/Projects/youtube-videos-code-examples/MCP-Labs/java/target/mcp-demo-1.0-SNAPSHOT.jar"
    ]
  }
}
```

#### Reference

https://github.com/danvega/javaone-mcp
