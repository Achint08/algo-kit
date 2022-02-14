# General pattern of recursion
# 1. There are one or more base cases that are directly solvable without the need for further recursion.
# 2. Each recursive call moves the solution progressively closer to a base case.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# Writing recursive function:
# 1. First figure out base cases and build upon that.
# 2. Figure out recursive steps. Remember, the subproblem should be smaller and eventually reach to some base case.
if __name__ == '__main__':
    print(fact(9))
