def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [int(i) for i in input().split(' ')]
    bubble_sort(arr)
    print(arr)


# Time complexity - O(n^2)
# Space complexity - O(1)
# In place algorithm
# Stable algorithm
