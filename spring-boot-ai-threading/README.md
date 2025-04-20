

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
    "Which city is known as the Big Apple?",
    "What is the national sport of Japan?",
    "How many legs does a spider have?",
    "What is the capital city of Australia?",
    "Who wrote To Kill a Mockingbird?",
    "What is the formula for the area of a circle?",
    "What is the largest desert in the world?",
    "What galaxy is Earth located in?",
    "How many sides does a hexagon have?",
    "What is the name of the longest bone in the human body?",
    "Which country is famous for the Eiffel Tower?",
    "Who is known as the Father of Computers?",
    "How many teeth does an adult human have?",
    "What is the main ingredient in guacamole?",
    "What is the capital city of Egypt?",
    "Which planet has rings around it?",
    "How many players are on a soccer team?",
    "What is the freezing point of water in Fahrenheit?",
    "What is the hardest natural substance on Earth?",
    "Which famous scientist developed the theory of relativity?",
    "What is the national flower of Japan?",
    "What is the name of the biggest planet in our solar system?",
    "Which vitamin is produced when a person is exposed to sunlight?",
    "What is the distance light travels in one year called?",
    "Which blood type is known as the universal donor?",
    "What is the name of the longest bone in the human body?"
]'
```