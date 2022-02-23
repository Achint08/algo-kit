# DP with bit masking is technique to store state in a way
# that can be handled easily. We would be playing around
# bit mask all the time. This also helps us to reduce the dimension
# of the state variables, which is what we need. ( For example,
# in the below case, we have reduced state variable to 1 from 2.)
#
#
# Bitmasking details - https://medium.com/analytics-vidhya/bits-bitmasking-62277789f6f5
#
#
# Job assignment problem
#


def get_set_bits(mask):
    count = 0
    while(mask):
        if mask & 1:
            count += 1
        mask >>= 1
    return count


def assign_job(cost_matrix):
    dp = []
    tasks = len(cost_matrix)
    for i in range(2**tasks):
        dp.append(float('inf'))

    dp[0] = 0

    for mask in range(2**tasks):
        x = get_set_bits(mask)
        for j in range(0, tasks):
            if not mask & 1 << j:
                dp[mask | (1 << j)] = min(
                    dp[mask | (1 << j)], cost_matrix[x][j] + dp[mask]
                )

    return dp[2**tasks - 1]


if __name__ == '__main__':
    n = 3
    cost = [[10, 20, 30], [50, 10, 64], [76, 50, 54]]
    print(assign_job(cost))
