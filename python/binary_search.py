# def binary_search(arr, l, r, x):
#     if l > r:
#         return None

#     mid = l + (r - l) // 2

#     if arr[mid] == x:
#         return mid
#     elif arr[mid] > x:
#         return binary_search(arr, l, mid - 1, x)
#     else:
#         return binary_search(arr, mid + 1, r, x)


def binary_search_iterative(arr, l, r, x):

    while(l <= r):
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1


arr = [2, 2, 3, 4, 10, 40]

print(binary_search_iterative(arr, 0, len(arr) - 1, 50))
