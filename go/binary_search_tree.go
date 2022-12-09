package main

import "fmt"

type Node struct {
	value int
	left  *Node
	right *Node
}

type BinarySearchTree struct {
	root *Node
}

func search(root *Node, key int) *Node {
	if root == nil || root.value == key {
		return root
	}

	if root.value < key {
		return search(root.right, key)
	}

	return search(root.left, key)
}

func insert(root *Node, key int) *Node {
	if root == nil {
		return &Node{
			value: key,
		}
	}

	if root.value < key {
		root.right = insert(root.right, key)
	} else {
		root.left = insert(root.left, key)
	}

	return root
}

func findSuccessor(root *Node) *Node {
	curr := root.right

	for curr.left != nil {
		curr = curr.left
	}

	return curr
}

func delete(root *Node, key int) *Node {
	if root == nil {
		return root
	} else if root.value < key {
		root.right = delete(root.right, key)
	} else if root.value > key {
		root.left = delete(root.left, key)
	} else {
		if root.left == nil && root.right == nil {
			return nil
		} else if root.left == nil {
			return root.right
		} else if root.right == nil {
			return root.left
		} else {
			successor := findSuccessor(root)
			root.value = successor.value
			delete(root.right, successor.value)
			return root
		}
	}

	return nil
}

func main() {

	root := &Node{
		value: 50,
	}

	binarySearchTree := &BinarySearchTree{
		root: root,
	}

	root = insert(binarySearchTree.root, 30)
	root = insert(binarySearchTree.root, 20)
	root = insert(binarySearchTree.root, 40)
	root = insert(binarySearchTree.root, 70)
	root = insert(binarySearchTree.root, 60)
	root = insert(binarySearchTree.root, 80)

	fmt.Println(search(binarySearchTree.root, 46) != nil)
	fmt.Println(search(binarySearchTree.root, 60) != nil)

}
