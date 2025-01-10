# Speech-to-Text Service

This project provides a REST API for transcribing audio files using FastAPI and Celery.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/speech-to-text-service.git
    cd speech-to-text-service
    ```

2. Build and start the services:
    ```sh
    docker-compose up --build
    ```

> The first transcription request may take longer because Faster Whisper will download the model.

### Usage

#### Send a Transcription Request

Use the following `curl` command to send a transcription request:

```sh
curl -X 'POST' \
  'http://localhost:8000/transcribe/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/audiofile'
```

#### Check the transcription status

```
curl -X 'GET' \
  'http://localhost:8000/transcribe/<PUT HERE THE TASK ID>/status' \
  -H 'accept: application/json'
```

### Useful address:

- API Doc: http://127.0.0.1:8000/docs
- Flower: http://127.0.0.1:5555