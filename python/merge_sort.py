def merge_sort(arr):

    n = len(arr)

    if n <= 1:
        return

    mid = n // 2

    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while(i < len(L) and j < len(R)):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while(i < len(L)):
        arr[k] = L[i]
        i += 1
        k += 1

    while(j < len(R)):
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [int(i) for i in input().split(' ')]
    merge_sort(arr)
    print(arr)


# Time complexity - O(n lg n)
# Space complexity - O(n)
# Not In place algorithm
# Stable algorithm
