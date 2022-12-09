package main

import (
	"fmt"
)

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

// Given a string S and a string T, find the minimum window in S which will contain all the characters in T.

func findMinSubstring(s1 string, s2 string) int {
	start, end := 0, 0

	counter := make(map[string]int)

	for _, ch := range s2 {
		chStr := string(ch)
		_, exists := counter[chStr]
		if exists {
			counter[chStr] += 1
		} else {
			counter[chStr] = 1
		}
	}

	count := len(s2)
	countS1 := len(s1)

	res := int(MaxUint >> 1)

	for end < countS1 {
		counter[string(s1[end])] -= 1

		if counter[string(s1[end])] >= 0 {
			count -= 1
		}

		end += 1

		for count == 0 {
			if end-start < res {
				res = end - start
			}

			counter[string(s1[start])] += 1

			if counter[string(s1[start])] > 0 {
				count += 1
			}
			start += 1
		}
	}

	return res
}

func main() {
	fmt.Println(findMinSubstring("ADOBECODEBANC", "ABC"))

}
