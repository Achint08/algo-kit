# General pattern for divide and conquer algorithms:
# def divide_and_conquer(input_list, l, r):
#   Some base condition
#   some_div_idx = divide(input_list)
#   some_conquer_1 = divide_and_conquer(input_list, l, some_div_idx)
#   some_conquer_2 = divide_and_conquer(input_list, some_div_idx + 1, r)
#   some_combine_step = combine(some_conquer_1, some_conquer_2)
#   return some_combine_step

# Basically divide and conquer is just like recursion, but with few extra steps
# where we divide and combine the results.
