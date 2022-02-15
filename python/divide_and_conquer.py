# General pattern for divide and conquer algorithms:
# def divide_and_conquer(input_list, l, r):
#   Some base condition
#   some_div_idx = divide(input_list)
#   some_conquer_1 = divide_and_conquer(input_list, l, some_div_idx)
#   some_conquer_2 = divide_and_conquer(input_list, some_div_idx + 1, r)
#   some_combine_step = combine(some_conquer_1, some_conquer_2)
#   return some_combine_step

# Divide means to break down the problem into smaller subproblems
# Conquer means to solve the subproblems
# Combine means to combine the solutions of subproblems or do some other operation in the problem

# Basically divide and conquer is just like recursion, but with few extra steps
# where we divide and combine the results.
# Important to learn induction
# Base case
# Assume f(n - 1) works
# Show that f(n) works using f(n - 1)

# Best example: Tower of hanoi
# Watch this video: https://www.youtube.com/watch?v=rf6uf3jNjbo

# Pro tip: Always remember to return, if applicable


def toh(n, source, aux, dest):
    if n == 1:
        print(source, dest)
        return
    # Divide and conquer
    toh(n - 1, source, dest, aux)
    # Combine
    print(source, dest)
    # Divide and conquer again
    toh(n - 1, aux, source, dest)


if __name__ == '__main__':
    toh(3, 'A', 'B', 'C')
