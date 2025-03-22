package org.example;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatModel;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

class Classification {
    private int request;
    private String category;

    // Getters and Setters
    public int getRequest() {
        return request;
    }

    public void setRequest(int request) {
        this.request = request;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    @Override
    public String toString() {
        return "Classification{" +
                "request=" + request +
                ", category='" + category + '\'' +
                '}';
    }
}

class ClassificationsWrapper {
    private List<Classification> classifications;

    // Getters and Setters
    public List<Classification> getClassifications() {
        return classifications;
    }

    public void setClassifications(List<Classification> classifications) {
        this.classifications = classifications;
    }
}
public class OpenAITaskClassifier {
    private static final String OPENAI_API_KEY = "";

    private static final String SYSTEM_PROMPT = """
        You are an AI assistant specialized in task classification. Your role is to analyze user requests and categorize them into predefined task types. Follow these guidelines:

        1. Classify each request into one of the following categories:
           - Information Request
           - Action Request
           - Opinion/Advice Request
           - Creative Content Request
           - Technical Support
           - Other (specify subcategory)

        2. Return your classifications in a structured JSON array format.

        3. Do not attempt to actually fulfill the user's requests - your sole purpose is classification.

        4. Each request should be classified separately in the output array.

        Remember to be precise and consistent in your classifications.
    """;

    private static final List<String> USER_PROMPTS = Arrays.asList(
            "Can you help me find information about renewable energy sources for a presentation I'm giving next week? I'm particularly interested in recent advancements in solar technology.",
            "Write a short story about a detective who can communicate with house plants. Make it funny but with a surprising twist at the end.",
            "I'm getting an error message when I try to install the latest update for my application. The message says 'Error code: 0x80070057' - what does this mean and how can I fix it?",
            "What do you think about investing in cryptocurrency right now? Is it a good idea for someone with moderate risk tolerance?",
            "Can you send an email to my team informing them that tomorrow's meeting has been rescheduled to 3:00 PM?"
    );

    public static void main(String[] args) {
        try {
            String response = classifyTasksBatch(USER_PROMPTS);
            ObjectMapper objectMapper = new ObjectMapper();

            ClassificationsWrapper container = objectMapper.readValue(response, ClassificationsWrapper.class);

            var items = container.getClassifications();
            for (int i = 0; i < items.size(); i++) {
                System.out.println(USER_PROMPTS.get(i));
                System.out.println("Category: " + items.get(i).getCategory());
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String classifyTasksBatch(List<String> userPrompts) throws IOException {
        OpenAIClient client = OpenAIOkHttpClient.builder()
                .apiKey(OPENAI_API_KEY)
                .build();


        StringBuilder userPrompt = new StringBuilder("Please classify each of the following user requests:\n\n");
        for (int i = 0; i < userPrompts.size(); i++) {
            userPrompt.append("REQUEST ").append(i + 1).append(": ").append(userPrompts.get(i)).append("\n\n");
        }
        userPrompt.append("Return the classifications as a JSON where each item includes the request number and its classification details.\n\n");
        userPrompt.append("""
            Example output:
            {
                "classifications": [
                    {
                        "request": 1,
                        "category": "Information Request"
                    },
                    {
                        "request": 2,
                        "category": "Creative Content Request"
                    }
                    ...
                ]
            }
        """);

        ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
                .addSystemMessage(SYSTEM_PROMPT)
                .addUserMessage(String.valueOf(userPrompt))
                .model(ChatModel.GPT_4O_MINI)
                .build();

        ChatCompletion chatCompletion = client.chat().completions().create(params);

        return chatCompletion.choices().getFirst().message().content().get();
    }
}
