# Docker Commands Documentation

This document provides a comprehensive guide to the Docker commands used for building, tagging, and pushing the IT Solutions static page Docker image to Docker Hub.

## Project Setup

Before building the Docker image, we created two important configuration files:

1. **Dockerfile** - Defines how the Docker image should be built
2. **.dockerignore** - Specifies which files and directories should be excluded from the Docker build context

## Building and Pushing the Docker Image

### 1. Building the Basic Docker Image

```bash
docker build -t it-solutions-static .
```

This command builds a Docker image from the Dockerfile in the current directory and tags it as `it-solutions-static`.

- `-t it-solutions-static`: Tags the image with the name "it-solutions-static"
- `.`: Specifies the build context (current directory)

### 2. Logging in to Docker Hub

```bash
docker login
```

This command initiates the Docker Hub login process. It will prompt for your Docker Hub credentials or open a web-based login flow.

### 3. Tagging the Image with Docker Hub Username

```bash
docker tag it-solutions-static johnidouglas/it-solutions-static:latest
```

This command creates a new tag for the existing image, preparing it for pushing to Docker Hub.

- `it-solutions-static`: The source image name
- `johnidouglas/it-solutions-static:latest`: The target image name with Docker Hub username and tag

### 4. Pushing the Image to Docker Hub

```bash
docker push johnidouglas/it-solutions-static:latest
```

This command pushes the tagged image to Docker Hub, making it publicly available.

### 5. Building and Pushing a Multi-Platform Image

```bash
docker buildx build --platform linux/amd64 -t johnidouglas/it-solutions-static:latest --push .
```

This command builds a Docker image specifically for the linux/amd64 platform and pushes it directly to Docker Hub.

- `--platform linux/amd64`: Specifies the target platform architecture
- `-t johnidouglas/it-solutions-static:latest`: Tags the image
- `--push`: Automatically pushes the image to Docker Hub after building
- `.`: Specifies the build context (current directory)

### 6. Verifying the Push

```bash
docker push johnidouglas/it-solutions-static:latest
```

This command verifies that the image has been successfully pushed to Docker Hub by attempting to push it again.

## Using the Docker Image

### Pulling the Image

```bash
docker pull johnidouglas/it-solutions-static:latest
```

This command pulls the image from Docker Hub to your local machine.

### Running the Container

```bash
docker run -p 8000:8000 johnidouglas/it-solutions-static:latest
```

This command runs a container from the image, mapping port 8000 of the container to port 8000 on the host machine.

### Using Docker Compose

As defined in the `compose.yaml` file, you can also run the container using Docker Compose:

```bash
docker-compose up
```

This will start the container according to the configuration in the `compose.yaml` file.

## Docker Hub Repository

The Docker image is publicly available at:
https://hub.docker.com/r/johnidouglas/it-solutions-static
