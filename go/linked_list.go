package main

import (
	"fmt"
)

type Node struct {
	next *Node
	key  int
}

type LinkedList struct {
	head *Node
}

func (linkedList *LinkedList) push(value int) {
	newNode := &Node{
		key: value,
	}

	newNode.next = linkedList.head
	linkedList.head = newNode
}

func (linkedList *LinkedList) insertAfter(prevNode *Node, value int) {
	if prevNode == nil {
		return
	}

	newNode := &Node{
		key: value,
	}

	newNode.next = prevNode.next
	prevNode.next = newNode
}

func (linkedList *LinkedList) append(value int) {

	newNode := &Node{
		key: value,
	}

	if linkedList.head == nil {
		linkedList.head = newNode
		return
	}

	last := linkedList.head
	for last.next != nil {
		last = last.next
	}

	last.next = newNode

}

func (linkedList *LinkedList) print() {

	curr := linkedList.head
	for curr != nil {
		fmt.Println(curr.key)
		curr = curr.next
	}
}

func (linkedList *LinkedList) delete(value int) {
	curr := linkedList.head

	if curr != nil && curr.key == value {
		linkedList.head = curr.next
		return
	}

	prev := &Node{}

	for curr != nil {
		if curr.key == value {
			prev.next = curr.next
			return
		}

		prev = curr
		curr = curr.next
	}
}

func main() {
	linkedList := LinkedList{}
	linkedList.append(6)
	linkedList.print()
	fmt.Println("-")
	linkedList.push(7)
	linkedList.print()
	fmt.Println("-")
	linkedList.push(1)
	linkedList.print()
	fmt.Println("-")
	linkedList.append(8)
	linkedList.print()
	fmt.Println("-")
	linkedList.insertAfter(linkedList.head.next.next, 2)
	linkedList.print()
	fmt.Println("-")
	linkedList.delete(1)
	linkedList.print()
	fmt.Println("-")
}
