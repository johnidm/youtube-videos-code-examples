
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;
using System.Net.Http;
using System.Net.Http.Json;
using System.Text.Json;
using System.Threading.Tasks;

var builder = Host.CreateApplicationBuilder(args);

builder.Logging.AddConsole(consoleLogOptions =>
{
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddHttpClient()
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();

await builder.Build().RunAsync();

[McpServerToolType]
public static class EchoTool
{
    [McpServerTool, Description("Fetches data for a specified CEP. CEP is a 8-digit code used in Brazil to identify addresses.")]
    public static async Task<string> FetchCep(
        HttpClient httpClient,
        [Description("The CEP to fetch data for.")] string cep,
        CancellationToken cancellationToken) {
        
        var response = await httpClient.GetAsync($"https://brasilapi.com.br/api/cep/v1/{cep}", cancellationToken);
        response.EnsureSuccessStatusCode();
        
        var jsonContent = await response.Content.ReadFromJsonAsync<JsonElement>(cancellationToken);
        return jsonContent.ToString();
    }
}
