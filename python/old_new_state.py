# Template - Very commonly used in DP
# def process_old(i, old, new):
#     pass

# def old_new_state(arr):
#     old, new = 0, 1
#     for i in range(len(arr)):
#         old, new = new, process_old(i, old, new)

# Calculate fibonacci number iteratively.

def fibonacci(n):
    old, new = 0, 1
    for _ in range(n - 1):
        old, new = new, old + new

    return new


if __name__ == '__main__':
    print(fibonacci(4))
