# All source Shortest Path Algorithm
# Floyd Warshall Algorithm
# Note:
# 1. Can detect negative cycle.

# Based on the idea of dynamic programming
def floyd_warshall(vertices, adj_list):

    dist = {}

    for vertice1 in vertices:
        dist[vertice1] = {}
        for vertice2 in vertices:
            dist[vertice1][vertice2] = float('inf')

    for vertice in vertices:
        dist[vertice][vertice] = 0

    for u in adj_list:
        for v in adj_list[u]:
            dist[u][v] = adj_list[u][v]

    for s in vertices:
        for m in vertices:
            for d in vertices:
                dist[s][d] = min(dist[s][d], dist[s][m] + dist[m][d])

    # If distance from node to itself is negative, then there is a negative cycle.

    for u in vertices:
        if dist[u][u] < 0:
            return True, []

    return False, dist


adj_list = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

vertices = adj_list.keys()

print(floyd_warshall(vertices, adj_list))


# Negative Weight Cycle.
adj_list = {
    'U': {'V': -2, 'W': 5, 'X': 1},
    'V': {'U': -2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(floyd_warshall(vertices, adj_list))
