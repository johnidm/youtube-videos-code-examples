# OpenAI Chat Assistent

This repository includes an example that demonstrates how to use the OpenAI Assistant.

### How to run 

```
make install-dependecies
```

```
OPENAI_API_KEY="sk-proj-..." make web
```

##### Dokcer 

```
make docker-push-chat-web
```

```
docker run -e OPENAI_API_KEY="sk-proj-..." -p 8501:8501 reg-img-unic.sienge.com.br/dev-core/sienge-magic-chat-web-core:latest
```
