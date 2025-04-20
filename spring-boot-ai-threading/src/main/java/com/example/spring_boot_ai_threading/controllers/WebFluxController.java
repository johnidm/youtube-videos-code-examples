package com.example.spring_boot_ai_threading.controllers;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.ArrayList;
import java.util.List;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity;

import org.springframework.web.bind.annotation.RequestMapping;

@RestController
@RequestMapping("/webflux")
public class WebFluxController {

    @PostMapping("/")
    public ResponseEntity<List<String>> webfluxEndpoint(@RequestBody List<String> prompts) {
        
        List<String> responses = new ArrayList<>();
        
        for (String prompt : prompts) {
            String response = generateResponse(prompt);
            responses.add(response);
        }
        
        return ResponseEntity.ok(responses);
    }

    private String generateResponse(String prompt) {
        return "[WebFlux] " + prompt;
    }

}
