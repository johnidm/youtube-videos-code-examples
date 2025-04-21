package com.example.app.controllers;

import java.time.Duration;
import java.time.Instant;
import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
@RequestMapping("/webflux")
public class WebFluxController {

    private final WebClient webClient;
    private final String model;

    public WebFluxController(WebClient.Builder webClientBuilder,
            @Value("${spring.ai.openai.api-key}") String apiKey,
            @Value("${spring.ai.openai.model}") String model, 
            @Value("${spring.ai.openai.base-url}") String baseUrl) {

        this.webClient = webClientBuilder
                .baseUrl(baseUrl)
                .defaultHeader("Authorization", "Bearer " + apiKey)
                .defaultHeader("Content-Type", "application/json")
                .build();

        this.model = model;
    }

    @PostMapping("/")
    public ResponseEntity<List<String>> webfluxEndpoint(@RequestBody List<String> prompts) {
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
        return webClient.post()
                .uri("/v1/chat/completions")
                .bodyValue(Map.of(
                        "model", model,
                        "messages", List.of(Map.of(
                                "role", "user",
                                "content", prompt
                        ))
                ))
                .retrieve()
                .bodyToMono(String.class)
                .map(response -> {
                    try {
                        ObjectMapper mapper = new ObjectMapper();
                        JsonNode node = mapper.readTree(response);
                        return node.get("choices").get(0).get("message").get("content").asText();
                    } catch (com.fasterxml.jackson.core.JsonProcessingException e) {
                        return "Error parsing response: " + e.getMessage();
                    }
                });
    }

}
