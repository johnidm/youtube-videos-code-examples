using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Text.Json;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.Google;

[assembly: Experimental("SKEXP0070")]

namespace GeminiLLM;

public class Seller
{
    [Description("The full legal name of the seller")]
    public string Name { get; set; }

    [Description("The full address of the seller")]
    public string Address { get; set; }
}

public class Buyer
{
    [Description("The full legal name of the buyer")]
    public string Name { get; set; }

    [Description("The full address of the buyer")]
    public string Address { get; set; }
}

public class Contract
{
    [Description("he full street address of the property")]
    public string PropertyAddress { get; set; }

    [Description("The total purchase price of the property")]
    public string PropertyPrice { get; set; }

    [Description("The full legal description of the property")]
    public string PropertyDescription { get; set; }

    [Description("The date the agreement was signed")]
    public string Date { get; set; }

    public Seller Seller { get; set; }
    public Buyer Buyer { get; set; }
}

[Experimental("SKEXP0070")]
public class Progarm
{
    public static async Task Main(string[] args)
    {
        var modelId = "gemini-2.0-flash";
        var apiKey = "your Gemini API Key";


        var builder = Kernel.CreateBuilder();

        builder.AddGoogleAIGeminiChatCompletion(modelId, apiKey);

        var kernel = builder.Build();

        var chatService = kernel.GetRequiredService<IChatCompletionService>();

        var file = "your PDF file";

        var bytes = File.ReadAllBytes(file);

        var history = new ChatHistory();

        history.AddSystemMessage(
            """
            You are an expert real estate contract analyst.  
            Your task is to extract key information from the provided real estate purchase agreement.  
            Pay close attention to detail and extract the following data points.  
            If a data point is not explicitly mentioned in the document, mark it as "N/A".
            Format your response as a JSON object, where the keys are the data point names and the values are the extracted information.  
            Do not include any explanatory text or comments in your response, just the raw JSON.
            The real estate purchase agreement is provided below. 
            Process it carefully and provide the JSON output.
            """
        );

        history.AddUserMessage([
            new TextContent("This is the PDF file"),
            new ImageContent(bytes, "application/pdf")
        ]);

        var executionSettings = new GeminiPromptExecutionSettings
        {
            MaxTokens = null,
            ResponseSchema = typeof(Contract),
            ResponseMimeType = "application/json"
        };

        var response = await chatService.GetChatMessageContentAsync(
            history, executionSettings);

        var contract = JsonSerializer.Deserialize<Contract>(response.ToString());
        Console.WriteLine(JsonSerializer.Serialize(contract, new JsonSerializerOptions { WriteIndented = true }));
        Console.WriteLine(response.Content);
    }
}