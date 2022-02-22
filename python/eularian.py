# Definitions:
# Eularian path -  Path that visited every edge exactly once.
# Eularian circuit - Eularian path that starts and ends at the same vertex.
# How to identify?
# Identify add connected components
# Total no. of odd degree vertices can't never be odd.
# Find all the connected vertices and check if:
# 1. Total odd degree vertices more than 2: None
# 2. 2 odd degree vertices - Path.
# 4. 0 odd degree vertices - Circuit
#
#
# Extra knowledge - Hamoltian Path is a path that visits every vertex exactly once.
# Likewise for hamoltian circuit, the source and destination vertex should match.
# There is no way to identify if graph has hamoltian path. Moreover, this forms the
# base question for Travelling salesman problem, such that the weights in minimal.


def eularian(adj_list):

    odd_count = 0

    for vertice in adj_list:
        if adj_list[vertice] and len(adj_list[vertice]) & 1:
            odd_count += 1

    if odd_count == 0:
        return "Circuit"
    elif odd_count == 2:
        return "Path"
    else:
        return "None"


if __name__ == '__main__':
    # None
    adj_list = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }

    print(eularian(adj_list))

    # Path
    adj_list = {
        'U': {'W': 5, 'X': 1},
        'V': {'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }

    print(eularian(adj_list))

    # Path
    adj_list = {
        'U': {'W': 5, 'X': 1},
        'V': {'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }

    print(eularian(adj_list))
