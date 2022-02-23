# How to identify problems, at first place?
# If the solution to a problem depends on the solutions of further sub-problems, then
# we should check that instead of checking solutions to all sub-problems, if we can
# make decision based on a local optimal solution, then we have greedy solution here.
# It's important to verify that our locally optimal solution will be the best solution
# from the solutions of sub-problems.
#
# Fractional Knapsack problem:
#
# Given weights and values of n items, we need to put these items in a knapsack of capacity
# W to get the maximum total value in the knapsack. We can break items for maximizing
# the total value of knapsack.
#
# Note:
# 1. You need to convert the problem in a way that it can be solved by greedy step. Greedy step
# won't be intuitive in first look. For example, in case of fractional knapsack, sorting unit weight
# and flexibility to choose fractional weight converts problem into greedy algo, otherwise,
# we would have to search the entire search space.
#

def fractional_knapsack(unit_val, weight, capacity):

    max_val = 0

    zipped_list = sorted(list(zip(unit_val, weight)), key=lambda x: x[0])

    for curr_unit_val, curr_weight in zipped_list[::-1]:
        if capacity - curr_weight >= 0:
            capacity -= curr_weight
            max_val += curr_weight * curr_unit_val
        else:
            max_val += capacity * curr_unit_val
            break

    return max_val


if __name__ == "__main__":
    total_wt = [10, 40, 20, 30]
    total_val = [60, 40, 100, 120]
    unit_per_val = [val//wt for wt, val in zip(total_wt, total_val)]
    cap = 50
    print(fractional_knapsack(unit_per_val, total_wt, cap))
