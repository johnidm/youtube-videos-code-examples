using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Text.Json;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.Google;

[assembly: Experimental("SKEXP0070")]

namespace GeminiLLM;

public class Produto
{
    public string Nome { get; set; }
    public string Subtitulo { get; set; }
    public string Marca { get; set; }
    public string Resumo { get; set; }
    public string Descrição { get; set; }
    public string Acabamento_Cores { get; set; }
    public string Aplicações { get; set; }
    public string Capacidades_Desempenho { get; set; }
    public string Composição { get; set; }
    public string Desempenho { get; set; }
    public string Dimensões_Peso { get; set; }
    public string Normas_Certificados { get; set; }
    public string Sustentabilidade { get; set; }
    public string Uso_Aplicações { get; set; }
    public string Vantagens { get; set; }
}

public class Produtos
{
    public List<Produto> Products { get; set; }
}

[Experimental("SKEXP0070")]
public class Progarm
{
    public static async Task Main(string[] args)
    {
        var modelId = "gemini-2.0-flash";
        var apiKey = "AIzaSyD-P3NkidGES847hc-HRveW5PbgGWngW1I";
        
        var builder = Kernel.CreateBuilder();

        builder.AddGoogleAIGeminiChatCompletion(modelId, apiKey);

        var kernel = builder.Build();

        var chatService = kernel.GetRequiredService<IChatCompletionService>();

        var file = "/home/johni.marangon@softplan.com.br/Downloads/codig-fernando/src/uploads/1411_catalogo_conexoes_em_ferro_fundido_galvanizadas_2020.pdf";

        var bytes = File.ReadAllBytes(file);

        var history = new ChatHistory();

        history.AddSystemMessage(
            """
            Tarefa:
            - Extraia o texto do PDF em anexo e estruture as informações dos produtos conforme as instruções abaixo.
            
            Instruções:
            - Gere um resumo conciso baseado exclusivamente nas informações presentes no texto.
            - O conteúdo será utilizado em um portal de e-commerce.
            - Não invente informações nem preencha lacunas com suposições. Utilize apenas os dados claramente identificáveis no texto.
            - Se um produto não possuir informações suficientes para um anúncio claro e atrativo, ignore-o.
            - Identifique corretamente a marca do produto:
            - Não inclua o nome do fabricante, a menos que fabricante e marca sejam a mesma entidade.
            - Se a marca estiver no nome do produto, utilize somente essa marca no campo "Marca".
            - Não altere o nome do produto sob nenhuma circunstância.
            
            Saída esperada:
            - Os dados devem ser extraídos e estruturados de forma organizada para facilitar seu uso na plataforma de e-commerce.
            """
        );

        history.AddUserMessage([
            new TextContent("Analise o seguinte texto extraído do PDF"),
            new ImageContent(bytes, "application/pdf")
        ]);

        var executionSettings = new GeminiPromptExecutionSettings
        {
            MaxTokens = null,
            ResponseSchema = typeof(Produtos),
            ResponseMimeType = "application/json"
        };

        var response = await chatService.GetChatMessageContentAsync(
            history, executionSettings);

        var contract = JsonSerializer.Deserialize<Produtos>(response.ToString());
        Console.WriteLine(JsonSerializer.Serialize(contract, new JsonSerializerOptions { WriteIndented = true }));
  
    }
}