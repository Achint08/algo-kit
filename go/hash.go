package main

import (
	"fmt"
)

type Set struct {
	m map[int]struct{}
}

var exists = struct{}{}

func newSet() *Set {
	set := &Set{}
	set.m = make(map[int]struct{})
	return set
}

func (set *Set) add(value int) {
	set.m[value] = exists
}

func (set *Set) delete(value int) {
	delete(set.m, value)
}

func (set *Set) contains(value int) bool {
	_, ok := set.m[value]

	return ok
}
func main() {
	hash_table := make(map[int]int)

	hash_table[1] = 2
	hash_table[2] = 3

	fmt.Println(hash_table)

	delete(hash_table, 2)
	fmt.Println(hash_table)

	hash_set := newSet()

	hash_set.add(2)
	hash_set.add(3)
	fmt.Println(hash_set.m)

	hash_set.delete(3)
	fmt.Println(hash_set.m)

}
