package main

import (
	"fmt"
)

func addEdge(adjMatrix [][]bool, source int, destination int) {
	adjMatrix[source][destination] = true
}

func main() {
	adjMatrix := [][]bool{}
	for idx := 0; idx < 4; idx++ {
		adjMatrix = append(adjMatrix, make([]bool, 4))
	}
	addEdge(adjMatrix, 1, 2)
	addEdge(adjMatrix, 2, 3)
	addEdge(adjMatrix, 3, 2)
	addEdge(adjMatrix, 0, 1)
	fmt.Println(adjMatrix)
}
