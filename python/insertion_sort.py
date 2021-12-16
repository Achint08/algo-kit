def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [int(i) for i in input().split(' ')]
    insertion_sort(arr)
    print(arr)


# Time complexity - O(n^2)
# Space complexity - O(1)
# In place algorithm
# Stable algorithm
