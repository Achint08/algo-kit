import bisect
# Always assume array is sorted

# Basics
# bisect_left
# Find a position where the element should be inserted to a position just left of it
# arr = [24, 33, 41, 41, 45, 50, 53, 59, 62, 66, 69]
# print(bisect.bisect_left(arr, 41))

# O(n) time operation
# arr = [24, 33, 41, 41, 45, 50, 53, 59, 62, 66, 69]
# bisect.insort_left(arr, 41)
# print(arr)


# arr = [1.1, 2.2, 3.3, 4.6, 5.5, 6.9]
# print(bisect.bisect_left(arr, 4.4))


# arr = ["aaa", "bbb", "ccc"]
# print(bisect.bisect_left(arr, "bug"))

# bisect_right
# Find a position where the element should be inserted to a position just right of it
# arr = [24, 33, 41, 41, 45, 50, 53, 59, 62, 66, 69]
# print(bisect.bisect_right(arr, 41))

# # O(n) time operation
# arr = [24, 33, 41, 41, 45, 50, 53, 59, 62, 66, 69]
# bisect.insort_right(arr, 41)
# print(arr)


# arr = [1.1, 2.2, 3.3, 4.6, 5.5, 6.9]
# print(bisect.bisect_right(arr, 4.4))


# arr = ["aaa", "bbb", "ccc"]
# print(bisect.bisect_right(arr, "bug"))


# bisect
# Find a position where the element should be inserted to a position just right of it
arr = [24, 33, 41, 41, 45, 50, 53, 59, 62, 66, 69]
print(bisect.bisect(arr, 41))

# O(n) time operation
arr = [24, 33, 41, 41, 45, 50, 53, 59, 62, 66, 69]
bisect.insort(arr, 41)
print(arr)

arr = [1.1, 2.2, 3.3, 4.6, 5.5, 6.9]
print(bisect.bisect(arr, 4.4))

arr = ["aaa", "bbb", "ccc"]
print(bisect.bisect(arr, "bug"))

# In short, bisect = bisect_right
