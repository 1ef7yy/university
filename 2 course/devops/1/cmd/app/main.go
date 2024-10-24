package main

import (
	"fmt"
	"net/http"
)

func main() {
	fmt.Println("Web server started!")

	http.ListenAndServe("localhost:8080", nil)
}
