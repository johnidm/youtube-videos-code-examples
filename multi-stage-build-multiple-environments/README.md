# Multi-stage build multiple environments

The idea is to create a single Dockerfile to build multiple environments (development, staging, production).

## Install deps

`pip install -r requirements.txt`

## Run app

`uvicorn main:app --reload`

## Build and Run with Dockerfile

### Development

```
docker build --target development -t fastapi-dev .
docker run --rm -p 8000:8000 fastapi-dev
```

### Production

```
docker build --target production -t fastapi-prod .
docker run --rm -p 8000:8000 fastapi-prod
```

## Build and Run with Docker compose

### Development

```
docker compose up app-dev
```

### Production

```
docker compose up app-prod
```
