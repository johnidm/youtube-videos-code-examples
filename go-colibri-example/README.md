

https://docs.colibriproject.dev.br/

Initialize Go module:

```
go mod init go-colibri-example
```

Get dependencies:

```
go get github.com/colibriproject-dev/colibri-sdk-go
```

Install dependencies:

```
go mod tidy
```

Run the application:

```
go run main.go
```

Test the application:

```
curl -X GET http://localhost:8080/users
```
