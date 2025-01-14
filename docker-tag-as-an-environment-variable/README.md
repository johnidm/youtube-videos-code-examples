## Accessing tag as an environment variable inside a Docker container project

If you need to know the current revision of Docker image in an API running inside the container you can use the docker build arguments combination with Docker variable environment.

> Look ARG and ENV instructions inside the Dockerfile.

### Follow the steps below to execute the proposed solution.

Build Docker image

```
export CI_TAG=v1.0.1
docker build --build-arg DOCKER_TAG=$CI_TAG -t my-app:$CI_TAG .
```

Running API
```
docker run -p 8080:8080 my-app:$CI_TAG
```

Access endpoint
```
curl -i http://0.0.0.0:8080 
```
