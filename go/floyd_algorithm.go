package main

import (
	"fmt"
)

func slowMovingCondition(arr []int, slow int, fast int) bool {
	return arr[slow] != arr[fast]
}

func processLogic(arr []int, slow int, fast int) {
	arr[slow] = arr[fast]
}

func floydAlgorithm(arr []int) int {
	slow := 0
	n := len(arr)

	for fast := 0; fast < n; fast++ {
		if slowMovingCondition(arr, slow, fast) {
			slow += 1
		}

		processLogic(arr, slow, fast)
	}

	return slow + 1
}

func main() {

	intArray := []int{1, 1, 2, 2, 2, 3, 4, 5}

	end_idx := floydAlgorithm(intArray)

	fmt.Println(intArray[:end_idx])
}
