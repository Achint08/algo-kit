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


def quick_select(arr, low, high, k):

    if k < 0 or k > high - low + 1:
        return

    pivot = partition(arr, low, high)
    if pivot - low == k - 1:
        return arr[pivot]
    elif pivot - low > k - 1:
        return quick_select(arr, low, pivot - 1, k)
    else:
        return quick_select(arr, pivot + 1, high, k + low - (pivot + 1))


if __name__ == '__main__':
    arr = [10, 4, 5, 8, 6, 11, 26]
    print(quick_select(arr, 0, len(arr) - 1, 3))
