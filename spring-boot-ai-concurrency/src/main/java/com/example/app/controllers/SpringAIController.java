package com.example.app.controllers;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.time.Duration;
import java.time.Instant;
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
        Instant start = Instant.now();

        Flux<String> iter = Flux.fromIterable(prompts)
                .flatMapSequential(this::generateResponseAsync, 100);

        List<String> results = iter.collectList().block();
        
        Instant end = Instant.now();
        Duration duration = Duration.between(start, end);

        System.out.println("Completed!");
        System.out.println("Duration: " + String.format("%.3f seconds", duration.toMillis() / 1000.0));
        System.out.println("Java Version: " + System.getProperty("java.version"));
        System.out.println("Responses size: " + results.size());

        return ResponseEntity.status(HttpStatus.CREATED).body(results);
    }

    private Mono<String> generateResponseAsync(String prompt) {
        return chatClient.prompt()
                .user(prompt)
                .stream()
                .content()
                .collectList()
                .map(chunks -> String.join("", chunks));
    }
}
