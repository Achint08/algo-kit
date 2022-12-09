/* Monotonic stack is basically a stack, which maintains the list of elements
 from left to right in a sorted order. It's good for problems like
 next/previous greatest/smallest element/range query. (e.g. left limit/right limit)
 E.g. Given an array of integers heights representing the histogram's bar height
 where the width of each bar is 1, return the area of the largest rectangle in the histogram.
*/

package main

import (
	"fmt"
	"errors"
)


type Arr struct {
	stack []int
}

func newStack() *Arr {
	arr := &Arr{}
	arr.stack = make([]int, 0)
	return arr
}

func (arr *Arr) push(value int) {
	arr.stack = append(arr.stack, value)
}

func (arr *Arr) isEmpty() bool {
	n := len(arr.stack)
	return n == 0
}

func (arr *Arr) pop() (int, error) {
	if arr.isEmpty() {
		return -1, errors.New("Stack underflow")
	}
	n := len(arr.stack) - 1
	el := arr.stack[n]
	arr.stack = append(arr.stack[:n])
	return el, nil
}

func (arr *Arr) top() (int, error) {
	if arr.isEmpty() {
		return -1, errors.New("Stack underflow")
	}
	n := len(arr.stack) - 1
	return arr.stack[n], nil
}

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func calcPrevSmaller(arr []int) []int {
	prevSmaller := make([]int, len(arr))
	stack := newStack()
	for idx:= 0; idx < len(arr); idx++ {
		top, _ := stack.top()
		for(!stack.isEmpty() && arr[top] >= arr[idx]) {
			stack.pop()
		}
		if stack.isEmpty() {
			prevSmaller[idx] = -1
			top, _ = stack.top()
		} else {
			top, _ = stack.top()
			prevSmaller[idx] = top
		}
		stack.push(idx)
	}

	return prevSmaller
}

func calcNextSmaller(arr []int) []int {
	nextSmaller := make([]int, len(arr))
	stack := newStack()
	for idx:= len(arr) - 1; idx >= 0; idx-- {
		top, _ := stack.top()
		for(!stack.isEmpty() && arr[top] >= arr[idx]) {
			stack.pop()
			top, _ = stack.top()
		}
		if stack.isEmpty() {
			nextSmaller[idx] = len(arr)
		} else {
			top, _ = stack.top()
			nextSmaller[idx] = top
		}
		stack.push(idx)
	}

	return nextSmaller
}

/* Basic idea is to pop elements until we find an element equal or more than
 its value. Then push the element. Such that an increasing order is maintained.
 We can perform action at every pop.
*/
func calculateMaximumHistrogramArea(arr []int) int {

	maxArea := 0
	prevSmaller := calcPrevSmaller(arr)
	nextSmaller := calcNextSmaller(arr)

	for idx := 0; idx < len(arr); idx++ {
		area := arr[idx] * (nextSmaller[idx] - prevSmaller[idx] - 1)
		maxArea = Max(maxArea, area)
	}

	return maxArea

}

func main() {
	arr := []int{2, 1, 5, 6, 2, 3}
	fmt.Println(calculateMaximumHistrogramArea(arr))
}