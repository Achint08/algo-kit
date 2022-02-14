from collections import deque


# Queue is the abstreact data structure
# which is used to order elements in FIFO order.

if __name__ == '__main__':
    queue = deque()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for el in arr:
        queue.append(el)

    while(queue):
        print(queue.popleft())
