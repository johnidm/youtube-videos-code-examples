# AI Threading

An example of how to use non-blocking requests to process multiple prompts concurrently.

## Docker 

```
# Set your OpenAI API key in your environment
export OPENAI_API_KEY=your_api_key_here

# Build and start the application
docker compose up --build
```

```
# Build the Docker image
docker build -t spring-boot-ai-threading .

# Run the container with your API key
docker run -p 8080:8080 -e OPENAI_API_KEY=your_api_key_here spring-boot-ai-threading
```

## Run the application

```
OPENAI_API_KEY=your_api_key ./mvnw spring-boot:run
```

or 

```
OPENAI_API_KEY=your_api_key mvn spring-boot:run
```

## API Documentation

http://localhost:8080/swagger-ui/index.html

## SpringAI Request Example

```
time curl -X 'POST' \
  'http://localhost:8080/springai/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '[
"What is the capital of Brazil?",
    "Who is the current President of the United States?",
    "What is the tallest mountain in the world?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "Who wrote the play Romeo and Juliet?",
    "What is the smallest prime number?",
    "Which language is spoken in Brazil?",
    "What is the currency of Japan?",
    "How many continents are there?",
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?",
    "Which animal is known as the king of the jungle?",
    "What is the square root of 64?",
    "What is the fastest land animal?",
    "Who discovered gravity?",
    "What year did the Titanic sink?",
    "Which country has the largest population?",
    "What is the longest river in the world?",
    "Who invented the telephone?",
    "What is the boiling point of water in Celsius?",
    "Which element has the atomic number 1?",
    "What is the main language spoken in Canada?",
    "Which city is known as the Big Apple?"
]'
```

## WebFlux Request Example

```
time curl -X 'POST' \
  'http://localhost:8080/webflux/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '[
    "What is the capital of Brazil?",
    "Who is the current President of the United States?",
    "What is the tallest mountain in the world?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "Who wrote the play Romeo and Juliet?",
    "What is the smallest prime number?",
    "Which language is spoken in Brazil?",
    "What is the currency of Japan?",
    "How many continents are there?",
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?",
    "Which animal is known as the king of the jungle?",
    "What is the square root of 64?",
    "What is the fastest land animal?",
    "Who discovered gravity?",
    "What year did the Titanic sink?",
    "Which country has the largest population?",
    "What is the longest river in the world?",
    "Who invented the telephone?",
    "What is the boiling point of water in Celsius?",
    "Which element has the atomic number 1?",
    "What is the main language spoken in Canada?",
    "Which city is known as the Big Apple?"
]'
```

## Benchmark Results

These are the results of both approaches running the same set of prompts.

- Execution Time (s): Total time taken by the controller function endpoint.
- Response Time (s): Total time taken for the endpoint request round trip.

### SpringAI

See the request in [SpringAI Request Example](#springai-request-example).

Sequence | Execution Time (s) | Response Time (s)
--- | --- | ---
1 | 3.964 | 4.173
2 | 4.827 | 4.927 
3 | 6.474 | 6.592 
4 | 3.904 | 3.999 
5 | 3.230 | 3.305 

### WebFlux

See the request in [WebFlux Request Example](#webflux-request-example).

Sequence | Execution Time (s) | Response Time (s)
--- | --- | ---
1 | 3.668 | 3.873
2 | 3.029 | 3.122 
3 | 3.519 | 3.599 
4 | 5.881 | 5.974 
5 | 2.795 | 2.877 

### Conclusion

WebFlux is 10% faster than SpringAI for this use case. This means that both approaches are efficient in terms of response time.
We can choose the approach that best fits our specific needs.