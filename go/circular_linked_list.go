package main

import (
	"fmt"
)

type Node struct {
	key  int
	next *Node
}

type CircularLinkedList struct {
	head *Node
}

func (circularLinkedList *CircularLinkedList) push(value int) {

	newNode := &Node{
		key: value,
	}

	if circularLinkedList.head == nil {
		circularLinkedList.head = newNode
		newNode.next = newNode
	}

	newNode.next = circularLinkedList.head

	curr := circularLinkedList.head

	for curr != nil {
		if curr.next == circularLinkedList.head {
			curr.next = newNode
			break
		}
		curr = curr.next
	}

	circularLinkedList.head = newNode

}

func (circularLinkedList *CircularLinkedList) print() {
	curr := circularLinkedList.head

	for curr.next != circularLinkedList.head {
		fmt.Println(curr.key)
		curr = curr.next
	}

	fmt.Println(curr.key)

	fmt.Println("-")
}

func main() {
	circularLinkedList := CircularLinkedList{}

	circularLinkedList.push(6)
	circularLinkedList.print()
	circularLinkedList.push(7)
	circularLinkedList.print()
	circularLinkedList.push(1)
	circularLinkedList.print()
}
