package main

import (
	"errors"
	"fmt"
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

func main() {
	stack := newStack()
	stack.push(1)
	fmt.Println(stack)
	fmt.Println("-")
	stack.push(2)
	fmt.Println(stack)
	fmt.Println("-")
	top, err := stack.top()
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println(top)
	}
	fmt.Println("-")
	el, err := stack.pop()
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println(el)
	}
	fmt.Println("-")
	fmt.Println(stack)
	fmt.Println("-")
	el, err = stack.pop()
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println(el)
	}
	fmt.Println("-")
	fmt.Println(stack)
	fmt.Println("-")
	el, err = stack.pop()
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println(el)
	}
	fmt.Println("-")
	fmt.Println(stack)
	fmt.Println("-")
}
