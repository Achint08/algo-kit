# Please check top-down_dp before bottom_up.
# Intuition of bottom up comes, generally, after finding the state definition in
# top-down DP.
#
# Key points:
# 1. We could have a lot of dimensions (state variables) using which we could solve
# in a bottom up manner. We should try to reduce the dimension, whenever possible
# and avoid dimensions which have a lot of states. Try to choose state variables
# which have limited states. For example, in 0-1 knapsack, we have 2 state variable
# capacity and curr_idx, both of which are limited.
# 2. Start with thinking of base cases, such as, in knapsack problem,
# let's assume we only have 1 item initially and try to think incrementally, what would
# happen if we know have two items, how would the solution to this problem depend of the
# solution of problem with 1 item. (Induction theorm comes into play here!)
# 3. We usually have a grid to store the space solutions, so as to use pre-computed results.
# Remember to initialize the grid.
#
# Learning DP takes time! Watch videos and read articles, practice makes perfect!! I am still in process,
# but that's what I have learned.
# My favorite playlists so far:
#
# 1. https://www.youtube.com/watch?v=YBSt1jYwVfU&list=PLl0KD3g-oDOGJUdmhFk19LaPgrfmAGQfo
# 2. https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go
#
# 0-1 Knapsack using bottom-up.

def knapsack(capacity):

    # It might help to create sentinels to help us in writing general solution.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(total_items + 1)]

    for item in range(1, total_items + 1):
        for curr_cap in range(1, capacity + 1):
            if curr_cap < total_wt[item - 1]:
                dp[item][curr_cap] = dp[item - 1][curr_cap]
            else:
                dp[item][curr_cap] = max(
                    dp[item - 1][curr_cap],
                    total_val[item - 1] +
                    dp[item - 1][curr_cap - total_wt[item - 1]]
                )
    return dp[total_items][capacity]


if __name__ == "__main__":
    total_wt = [10, 40, 20, 30]
    total_val = [60, 40, 100, 120]
    total_items = len(total_wt)
    cap = 50
    print(knapsack(cap))
