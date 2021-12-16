def counting_sort(arr):
    n = len(arr)

    min_el = arr[0]
    max_el = arr[0]

    for i in range(n):
        if arr[i] < min_el:
            min_el = arr[i]
        if arr[i] > max_el:
            max_el = arr[i]

    count = [0] * (max_el - min_el + 1)
    output = [0] * n

    for i in range(n):
        count[arr[i] - min_el] += 1

    for i in range(1, max_el - min_el + 1):
        count[i] += count[i - 1]

    i = n - 1

    while(i >= 0):
        output[count[arr[i] - min_el] - 1] = arr[i]
        count[arr[i] - min_el] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


if __name__ == '__main__':
    arr = [int(i) for i in input().split(' ')]
    counting_sort(arr)
    print(arr)


# Time complexity - O(n)
# Space complexity - O(n)
# Not In place algorithm
# Stable algorithm
