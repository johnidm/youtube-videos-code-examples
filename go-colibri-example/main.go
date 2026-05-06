package main

import (
	"net/http"

	"github.com/colibriproject-dev/colibri-sdk-go"
	"github.com/colibriproject-dev/colibri-sdk-go/pkg/web/restserver"
)

func beforeEnterExample(ctx restserver.WebContext) *restserver.MiddlewareError {
	return nil
}

type UserResp struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

var userRoutes = []restserver.Route{
	{
		URI:    "users",
		Method: http.MethodGet,
		Prefix: restserver.PublicApi,
		Function: func(ctx restserver.WebContext) {
			body := UserResp{Name: "John", Age: 30}
			ctx.JsonResponse(http.StatusOK, &body)
		},
		BeforeEnter: beforeEnterExample,
	},
}

func main() {
	// Inicializa as configurações, logs e conexões base
	colibri.InitializeApp()

	// Sua lógica de negócio aqui...
	restserver.AddRoutes(userRoutes)

	// Inicia o servidor web (porta padrão: 8080)
	restserver.ListenAndServe()
}
