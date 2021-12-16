def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low, high):

    if low >= high:
        return

    p = partition(arr, low, high)

    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)


if __name__ == '__main__':
    arr = [int(i) for i in input().split(' ')]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


# Time complexity - O(n lg n)
# Space complexity - O(1)
# In place algorithm
# Not Stable algorithm
