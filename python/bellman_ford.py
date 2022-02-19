# Single Soure Shortest Path Algorithm
# Bellman Ford Algorithm
# Note -
# 1. It works on negative weight.
# 2. Can detect negative cycle

# More inclined towards dynamic programming approach.
# The key idea is that it would take at most | V -1 | steps
# to know the minimum distance.
def bellman_ford(source, vertices, adj_list):
    dist = {}
    parent = {}
    for vertice in vertices:
        dist[vertice] = float('inf')
        parent[vertice] = None

    dist[source] = 0

    n = len(vertices)
    for _ in range(n - 1):

        for u in adj_list:
            for v in adj_list[u]:
                new_dist = adj_list[u][v]
                if new_dist + dist[u] < dist[v]:
                    dist[v] = dist[u] + new_dist
                    parent[v] = u

    for u in adj_list:
        for v in adj_list[u]:
            new_dist = adj_list[u][v]
            if new_dist + dist[u] < dist[v]:
                return True, {}, {}

    return False, dist, parent


adj_list = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

vertices = adj_list.keys()

print(bellman_ford('U', vertices, adj_list))


# Negative Weight Cycle.
adj_list = {
    'U': {'V': -2, 'W': 5, 'X': 1},
    'V': {'U': -2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(bellman_ford('U', vertices, adj_list))
