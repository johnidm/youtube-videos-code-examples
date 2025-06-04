package com.example.extract_data_from_pdf.controller;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.Map;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.core.io.InputStreamResource;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.util.MimeTypeUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class RootController {

    private final ChatClient chatClient;

    private final ChatModel chatModel;

    public RootController(ChatModel chatModel, ChatClient.Builder chatClientBuilder) {
        this.chatModel = chatModel;
        this.chatClient = chatClientBuilder.build();

    }

    @GetMapping("/")
    public String root() {
        return "Welcome to PDF Data Extraction API";
    }

    // @PostMapping(value="/carCounts", consumes =
    // MediaType.MULTIPART_FORM_DATA_VALUE, produces =
    // MediaType.APPLICATION_JSON_VALUE)
    // public carCounts(
    // @Parameter(description = "File to be uploaded", required = true)
    // @RequestParam("file") MultipartFile file, @RequestParam("colors") String
    // colors) {
    // try (InputStream inputStream = file.getInputStream()) {
    // var carCount = carCountService.countCar(inputStream, file.getContentType(),
    // colors);
    // return ResponseEntity.ok(carCount);
    // } catch (IOException e) {
    // return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error
    // uploading file");
    // }
    // }

    @PostMapping("/ner")
    public ResponseEntity<?> ner(@RequestParam("file") MultipartFile file) throws FileNotFoundException {

        String systemText = """
                Você é um assistente que extrai dados específicos de boletos e documentos para pagamento.

                Você receberá o conteúdo de um documento a ser pago.

                Regras:
                - As datas devem ser retornadas no formato **dd/mm/aaaa**.
                - O **sacado** é a pessoa ou empresa que deve pagar o título.
                - **CNPJ** são válidos com 14 dígitos numéricos. Exemplo: 34.877.404/0001-80
                - **CPF** são válidos com 11 dígitos numéricos. Exemplo: 100.993.400-70
                - Formato inválido de CNPJ: 1840969662/2025 (Documento de Arrecadação Municipal - D.A.M.)
                - Formato inválido de CNPJ: 83690000001-6 (chunk do código de barras)
                - **Não gere números para campos que não foram encontrados no documento.**
                - Se não conseguir extrair os dados, retorne o campo como **string vazia** (`""`), ou `0.0` no caso de valores numéricos.

                Retorne os dados extraídos em formato **JSON**, seguindo o schema abaixo:

                ```json
                {
                "cnpj_beneficiario": "string",
                "nome_beneficiario": "string",
                "cpf_cnpj_empresa_sacado": "string",
                "nome_empresa_sacado": "string",
                "numero_documento": "string",
                "data_documento": "string",
                "data_emissao": "string",
                "valor_total_documento": 0.0,
                "valor_desconto": 0.0,
                "data_vencimento": "string"
                }

                """;

        try (InputStream inputStream = file.getInputStream()) {
            String response = chatClient.prompt()
                    .system(systemText)

                    .user(userMessage -> userMessage
                            .text("Boleto de pagamento:")
                            .media(MimeTypeUtils.parseMimeType(file.getContentType()),
                                    new InputStreamResource(inputStream)))
                    .call().content();

            return ResponseEntity.ok(response);
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error uploading image");
        }

    }

    @GetMapping("/chat")
    public String chat() {
        String userText = """
                Tell me about three famous pirates from the Golden Age of Piracy and why they did.
                Write at least a sentence for each pirate.
                """;

        Message userMessage = new UserMessage(userText);

        String systemText = """
                You are a helpful AI assistant that helps people find information.
                Your name is {name}
                You should reply to the user's request with your name and also in the style of a {voice}.
                """;

        String name = "John";
        String voice = "experienced historian";

        SystemPromptTemplate systemPromptTemplate = new SystemPromptTemplate(systemText);
        Message systemMessage = systemPromptTemplate.createMessage(Map.of("name", name, "voice", voice));

        Prompt prompt = new Prompt(List.of(userMessage, systemMessage));

        ChatResponse response = chatModel.call(prompt);

        return response.getResult().getOutput().getText();

    }

}