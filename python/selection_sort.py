def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]


if __name__ == '__main__':
    arr = [int(i) for i in input().split(' ')]
    selection_sort(arr)
    print(arr)

# Time complexity - O(n^2)
# Space complexity - O(1)
# In place algorithm
# Stable algorithm
