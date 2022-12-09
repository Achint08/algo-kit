/* Implemented using doubly linked list
*/

package main

import (
	"container/list"
	"fmt"
)

func main() {
	queue := list.New()

	queue.PushBack(8)
	queue.PushBack(6)

	front := queue.Front()
	fmt.Println(front.Value)

	queue.Remove(front)

	front = queue.Front()
	fmt.Println(front.Value)
	
}