package com.example;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerFeatures;
import io.modelcontextprotocol.server.McpSyncServer;
import io.modelcontextprotocol.server.transport.StdioServerTransportProvider;
import io.modelcontextprotocol.spec.McpSchema;

public class App {
  public static void main(String[] args) throws IOException, InterruptedException {
    var transportProvider = new StdioServerTransportProvider(new ObjectMapper());

    var syncToolSpecification = getSyncToolSpecification();

    McpSyncServer server = McpServer.sync(transportProvider)
        .serverInfo("Java MCP Server Demo", "1.0.0")
        .capabilities(McpSchema.ServerCapabilities.builder()
            .tools(true)
            .logging()
            .build())
        .tools(syncToolSpecification)
        .build();

  }

  private static McpServerFeatures.SyncToolSpecification getSyncToolSpecification() {
    var schema = """
        {
          "type" : "object",
          "properties" : {
            "cep" : {
              "type" : "string",
              "description": "The Brazilian postal code (CEP) to look up (e.g., '01001000')"
            }
          },
          "required": ["cep"]
        }
        """;

    var syncToolSpecification = new McpServerFeatures.SyncToolSpecification(
        new McpSchema.Tool("fetch_cep",
            "Fetch data for a specified CEP. CEP is a 8-digit code used in Brazil to identify addresses.", schema),
        (exchange, arguments) -> {
          try {
            String cep = (String) arguments.get("cep");
            String response = getCepInfo(cep);
            return new McpSchema.CallToolResult(response, false);
          } catch (Exception e) {
            return new McpSchema.CallToolResult("Error fetching CEP info: " + e.getMessage(), true);
          }
        });
    return syncToolSpecification;
  }

  private static String getCepInfo(String cep) throws IOException, InterruptedException {

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://brasilapi.com.br/api/cep/v1/" + cep))
        .GET()
        .build();

    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

    ObjectMapper mapper = new ObjectMapper();
    return mapper.writeValueAsString(mapper.readValue(response.body(), Map.class));
  }
}
