package com.example.spring_boot_ai_threading.controllers;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/springai")
public class SpringAIController {

    private final ChatClient chatClient;

    public SpringAIController(ChatClient.Builder chatClientBuilder) {
        this.chatClient = chatClientBuilder.build();
    }

    @PostMapping("/")
    public ResponseEntity<List<String>> springAiEndpoint(@RequestBody List<String> prompts) {
        List<String> responses = new ArrayList<>();
        
        for (String prompt : prompts) {
            String response = generateResponse(prompt);
            responses.add(response);
        }
        
        return ResponseEntity.ok(responses);
    }

    private String generateResponse(String prompt) {
        return chatClient.prompt()
                .user(prompt)
                .call()
                .content();
    }

}
