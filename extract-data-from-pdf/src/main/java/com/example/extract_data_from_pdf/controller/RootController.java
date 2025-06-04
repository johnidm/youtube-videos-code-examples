package com.example.extract_data_from_pdf.controller;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import javax.imageio.ImageIO;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.rendering.PDFRenderer;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.ai.content.Media;
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

    @PostMapping("/ner")
    public ResponseEntity<?> ner(@RequestParam("file") MultipartFile file) throws FileNotFoundException {

        String systemText = """
        Você é um assistente especializado na extração de informações estruturadas a partir de documentos financeiros brasileiros, especialmente boletos bancários.
        Seu objetivo é analisar a(s) imagem(s) e extrair os principais campos.
        """;

        String userText = """
        Boletos:
        """;


        List<Media> images = new ArrayList<>();

        try (InputStream inputStream = file.getInputStream()) {
            PDDocument document = PDDocument.load(inputStream);
            PDFRenderer pdfRenderer = new PDFRenderer(document);

            for (int page = 0; page < document.getNumberOfPages(); ++page) {
                BufferedImage image = pdfRenderer.renderImageWithDPI(page, 300); // 300 DPI gives high quality
                String pathname = "/home/johni.marangon@softplan.com.br/Desktop/output_page_" + (page + 1) + ".png";
                ImageIO.write(image, "png", new File(pathname));
            }
            document.close();

            for (int page = 0; page < document.getNumberOfPages(); ++page) {
                String pathname = "/home/johni.marangon@softplan.com.br/Desktop/output_page_" + (page + 1) + ".png";

                File imageFile = new File(pathname);
                byte[] imageBytes = Files.readAllBytes(imageFile.toPath());

                images.add(
                        Media.builder().id("page" + page + 1)
                                .mimeType(MimeTypeUtils.IMAGE_PNG)
                                .data(imageBytes)
                                .build());

            }

            UserMessage u = UserMessage.builder().text(userText).media(images).build();
            String response = chatClient.prompt()
                    .system(systemText)
                    .messages(u)
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