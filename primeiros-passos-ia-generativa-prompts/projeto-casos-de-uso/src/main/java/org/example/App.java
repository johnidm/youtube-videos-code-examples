package org.example;


import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.Base64;
import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class App
{

    private static final String OPENAI_API_URL = "https://api.openai.com/v1/chat/completions";
    private static final String OPENAI_API_KEY = "";

    public static String generate(String systemPrompt,
                           String userPrompt,
                           Double temperature,
                           String model,
                           String fileName) throws IOException, InterruptedException {

        Path filePath = Paths.get(fileName);

        if (!Files.exists(filePath)) {
            throw new IOException("File not found: " + fileName);
        }

        String baseName = filePath.getFileName().toString();

        byte[] fileData = Files.readAllBytes(filePath);
        String base64Data = Base64.getEncoder().encodeToString(fileData);

        Map<String, Object> requestBody = Map.of(
                "model", model,
                "messages", List.of(
                        Map.of(
                                "role", "system",
                                "content", List.of(
                                        Map.of(
                                                "type", "text",
                                                "text", systemPrompt
                                        )
                                )
                        ),
                        Map.of(
                                "role", "user",
                                "content", List.of(
                                        Map.of("type", "text", "text", userPrompt),
                                        Map.of(
                                                "type", "file",
                                                "file", Map.of(
                                                        "file_data", "data:application/pdf;base64," + base64Data,
                                                        "filename", baseName
                                                )
                                        )
                                )
                        )
                )
        );

        ObjectMapper objectMapper = new ObjectMapper();

        String jsonPayload = objectMapper.writeValueAsString(requestBody);

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(OPENAI_API_URL))
                .header("Content-Type", "application/json")
                .header("Authorization", "Bearer " + OPENAI_API_KEY)
                .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
                .timeout(Duration.ofMinutes(10))
                .build();

        HttpClient httpClient = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(30))
                .build();

        HttpResponse<String> response = httpClient.send(request,
                HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new RuntimeException("OpenAI API error: " + response.statusCode() +
                    " - " + response.body());
        }

        JsonNode responseJson = objectMapper.readTree(response.body());

        JsonNode messageContent = responseJson
                .path("choices")
                .get(0)
                .path("message")
                .path("content");

        return messageContent.asText();
    }
    public static void main( String[] args ) throws IOException, InterruptedException {
        String systemPrompt = """
        Você é um assistente que extrai dados de boletos bancários.
        
        Sua resposta deve no formato JSON:
        {
            "pagador" : "", // Dados do pagador
            "beneficiário" : "", // Dados do beneficiário
            "dataVencimento" : "", // Data do vencimento do boleto
            "valor" : "", // Valor do documento
            "outrosDetalhes" : ["", ""] // Outros detalhes presentes no documento
            
        }   
        """;
        String userPrompt = "Arquivo:";
        Double temperature = 0.3;
        String model = "gpt-4.1-mini";

        String fileName = "/Users/johnimarangon/Projects/youtube-videos-code-examples/primeiros-passos-ia-generativa-prompts/Modelo-de-Boleto.pdf";

        String response = generate(
                systemPrompt,
                userPrompt,
                temperature,
                model,
                fileName);

        System.out.println(response);

    }
}
