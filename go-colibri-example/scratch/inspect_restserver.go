package main

import (
	"fmt"
	"github.com/colibriproject-dev/colibri-sdk-go/pkg/web/restserver"
)

func main() {
	fmt.Printf("PublicApi: %s\n", restserver.PublicApi)
	fmt.Printf("PrivateApi: %s\n", restserver.PrivateApi)
}
