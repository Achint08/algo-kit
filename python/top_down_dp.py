# Dynamic programming looks like backtracking problem, just that,
# some subproblems are getting repeated, i.e., some states occur again
# and again, so we need to avoid these repetition. Moreover, the solution
# to a problem at some state, depends on the solution of sub-problems, i.e., checking
# all the solutions from that state. In short, there are two properties:
#
# 1. Repetitions
# 2. For global optimal solution at some state, we need to
# check entire state sub-problem space orginating from that state. Sub-problem looks
# similar to the original problem.
#
# How to approach?
# 1. Define the state. The state should similar at each stage, so that it can be solved repetition.
# Also, define a sequence to reduce dimension and make solution more organized.
# 2. Store the result of some state, to avoid repetitions.
#
#  0-1 Knapsack problem:
#
#
# Given weights and values of n items, put these items in a knapsack of capacity W to get
# the maximum total value in the knapsack.


from functools import cache


# DP(we are storing results of a subproblem)

# A state is defined as knapsack with capacity C and the items starting from
# the index idx.
@cache
def knapsack(capacity, curr_item_idx):

    if capacity == 0 or curr_item_idx == total_items:
        return 0

    if capacity - total_wt[curr_item_idx] < 0:
        return knapsack(capacity, curr_item_idx + 1)

    return max(
        total_val[curr_item_idx] +
        knapsack(capacity - total_wt[curr_item_idx], curr_item_idx + 1),
        knapsack(capacity, curr_item_idx + 1)
    )


if __name__ == "__main__":
    total_wt = [10, 40, 20, 30]
    total_val = [60, 40, 100, 120]
    total_items = len(total_wt)
    cap = 50
    print(knapsack(cap, 0))
