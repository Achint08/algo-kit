# Monotonic stack is basically a stack, which maintains the list of elements
# from left to right in a sorted order. It's good for problems like
# next/previous greatest/smallest element/range query. (e.g. left limit/right limit)
# E.g. Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.

def calc_prev_smaller(arr):
    '''
    Calculates prev smaller for each index
    '''
    prev_smaller = []
    stack = []
    for idx, _ in enumerate(arr):
        while (stack and arr[stack[-1]] >= arr[idx]):
            stack.pop()

        if not stack:
            prev_smaller.append(-1)
        else:
            prev_smaller.append(idx)

        stack.append(idx)

    return prev_smaller


def calc_next_smaller(arr):
    '''
    Calculates next smaller for each index
    '''
    next_smaller = []
    stack = []
    for idx, _ in enumerate(arr):
        while (stack and arr[stack[-1]] >= arr[idx]):
            stack.pop()

        if not stack:
            next_smaller.append(len(arr))
        else:
            next_smaller.append(idx)

        stack.append(idx)

    return next_smaller


def cal_max_histogram_area(arr):
    '''
    Basic idea is to pop elements until we find an element equal or more than
    its value. Then push the element. Such that an increasing order is maintained.
    We can perform action at every pop.
    '''

    max_area = 0
    prev_smaller = calc_prev_smaller(arr)
    next_smaller = calc_next_smaller(arr)
    for i, _ in enumerate(arr):
        area = arr[i] * (next_smaller[i] - prev_smaller[i] - 1)
        max_area = max(max_area, area)

    return max_area


if __name__ == '__main__':
    A = [2, 1, 5, 6, 2, 3]
    print(cal_max_histogram_area(A))
