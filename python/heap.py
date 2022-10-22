import heapq

# This is a min heap.
# To use it as max heap, just add -ve sign to every element and use accordingly
a = [2, 4, 5, 1, 8, 9]
heapq.heapify(a)
print(a)
# push
heapq.heappush(a, 5)
print(a)
# pop
heapq.heappop(a)
print(a)
# push pop
heapq.heappushpop(a, 9)
print(a)
# replace - pop push
heapq.heapreplace(a, 10)
print(a)
# nlargest
print(heapq.nlargest(2, a))
# nsmallest
print(heapq.nsmallest(5, a))
# merge two unsorted arrays (returns heap)
m = list(heapq.merge(a, [5, 3]))
print(m)
