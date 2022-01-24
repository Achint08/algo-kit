# ## Template
# def slow_moving_condition(el1, el2):
#     # some condition

# def process_logic(s, f):
#     # some condition

# def slow_fast_pointer(arr):
#     slow = 0
#     for fast in range(len(arr)):
#         if slow_moving_condition(slow, fast):
#             slow += 1
#         process_logic(slow, fast)

# Can be used vica-versa as well

# Given a sorted array nums, remove the duplicates in place
# such that each element appear only once and return the new length.

def slow_moving_condition(arr, slow, fast):
    return arr[slow] != arr[fast]


def process_logic(arr, slow, fast):
    arr[slow] = arr[fast]


def floyd_algo(arr):
    slow = 0
    n = len(arr)
    for fast in range(1, n):
        if slow_moving_condition(arr, slow, fast):
            slow += 1

        process_logic(arr, slow, fast)

    return slow + 1


if __name__ == '__main__':
    arr = [int(el) for el in input().split(' ')]
    end_idx = floyd_algo(arr)
    print(arr[:end_idx])
