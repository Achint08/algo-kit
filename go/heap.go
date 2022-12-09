package main

import (
	"container/heap"
	"fmt"
)

type Element struct {
	priority int
	value    int
}

type PriorityQueue []Element

func (priorityQueue PriorityQueue) Len() int {
	return len(priorityQueue)
}

func (priorityQueue PriorityQueue) Swap(i, j int) {
	priorityQueue[i], priorityQueue[j] = priorityQueue[j], priorityQueue[i]
}

func (priorityQueue PriorityQueue) Less(i, j int) bool {
	return priorityQueue[i].priority >= priorityQueue[j].priority
}

func (priorityQueue *PriorityQueue) Push(element interface{}) {
	newElement := element.(Element)
	*priorityQueue = append(*priorityQueue, newElement)
}

func (priorityQueue *PriorityQueue) Pop() interface{} {
	temp := *priorityQueue
	l := len(temp)
	res := temp[l-1]
	temp[l-1] = Element{}
	*priorityQueue = temp[:l-1]
	return res
}

func topKFrequent(nums []int, k int) (res []int) {
	counter := make(map[int]int, 0)

	for idx := 0; idx < len(nums); idx++ {
		counter[nums[idx]] += 1
	}

	priorityQueue := make(PriorityQueue, 0)

	idx := 0

	for value, count := range counter {
		priorityQueue = append(priorityQueue, Element{
			value:    value,
			priority: count,
		})
		idx += 1
	}

	heap.Init(&priorityQueue)

	for i := 0; i < k; i++ {
		num := heap.Pop(&priorityQueue).(Element)
		res = append(res, num.value)
	}

	return res
}

func main() {
	a := []int{1, 1, 2, 4, 5, 1, 2}
	k := 3
	fmt.Println(topKFrequent(a, k))
}
