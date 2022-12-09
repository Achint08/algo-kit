package main

import (
	"fmt"
)

func addEdge(adjList map[int][]int, source int, destination int) {
	adjList[source] = append(adjList[source], destination)
}

func main() {
	adjList := make(map[int][]int)
	addEdge(adjList, 1, 2)
	addEdge(adjList, 2, 3)
	addEdge(adjList, 5, 6)
	addEdge(adjList, 2, 1)
	fmt.Println(adjList)
	return
}
