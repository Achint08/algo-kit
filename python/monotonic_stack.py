# Monotonic stack is basically a stack, which maintains the list of elements
# from left to right in a sorted order. It's good for problems like
# next/previous greatest/smallest element/range query. (e.g. left limit/right limit)
# E.g. Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.

def cal_max_histogram_area(arr):
    '''
    Basic idea is to pop elements until we find an element equal or more than
    its value. Then push the element. Such that an increasing order is maintained.
    We can perform action at every pop.
    '''

    stack = []
    stack.append(-1)
    max_area = 0
    for i in range(len(arr)):
        while(stack[-1] != -1 and arr[stack[-1]] > arr[i]):
            curr_idx = stack.pop()
            curr_height = arr[curr_idx]
            curr_width = i - stack[-1] - 1
            area = curr_height * curr_width
            max_area = max(area, max_area)
        stack.append(i)

    return max_area


if __name__ == '__main__':
    arr = [2, 1, 5, 6, 2, 3]
    print(cal_max_histogram_area(arr))
