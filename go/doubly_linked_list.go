package main

import (
	"fmt"
)

type Node struct {
	key int
	prev *Node
	next *Node
}

type DoublyLinkedList struct {
	head *Node
}

func (doublyLinkedList *DoublyLinkedList) push(value int) {
	newNode := &Node{
		key: value,
	}
	newNode.next = doublyLinkedList.head

	if doublyLinkedList.head != nil {
		doublyLinkedList.head.prev = newNode
	}

	doublyLinkedList.head = newNode
}

func (doublyLinkedList *DoublyLinkedList) insertAfter(prevNode *Node, value int) {
	newNode := &Node {
		key: value,
	}
	newNode.next = prevNode.next
	prevNode.next = newNode
	newNode.prev = prevNode

	if newNode.next != nil {
		newNode.next.prev = newNode
	}
}

func (doublyLinkedList *DoublyLinkedList) append(value int) {

	newNode := &Node {
		key: value,
	}
	curr := doublyLinkedList.head

	if curr == nil {
		doublyLinkedList.head = newNode
		return
	}

	for curr.next != nil {
		curr = curr.next
	}

	curr.next = newNode
	newNode.prev = curr

}

func (doublyLinkedList *DoublyLinkedList) print() {
	curr := doublyLinkedList.head

	for curr != nil {
		fmt.Println(curr.key)
		curr = curr.next
	}
	fmt.Println("-")
}

func (doublyLinkedList *DoublyLinkedList) delete(value int) {
	curr := doublyLinkedList.head

	if curr != nil && curr.key == value {
		doublyLinkedList.head = curr.next
		if doublyLinkedList.head != nil {
			doublyLinkedList.head.prev = nil
		}
		return
	}

	for curr != nil {
		if curr.key == value {
			curr.prev.next = curr.next
			if curr.next != nil {
				curr.next.prev = curr.prev
			}
		}
		curr = curr.next
	}

}

func main() {

	doublyLinkedList := DoublyLinkedList{}

	doublyLinkedList.push(2)
	doublyLinkedList.print()
	doublyLinkedList.push(7)
	doublyLinkedList.print()
	doublyLinkedList.push(8)
	doublyLinkedList.print()
	doublyLinkedList.push(10)
	doublyLinkedList.print()
	doublyLinkedList.append(4)
	doublyLinkedList.print()
	doublyLinkedList.delete(8)
	doublyLinkedList.print()
}