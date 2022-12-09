package main

import (
	"fmt"
)

func fib(n int) int {
	old, new := 0, 1

	for idx := 0; idx < n; idx++ {
		old, new = new, old+new
	}

	return old
}

func main() {
	fmt.Print(fib(10))
}
