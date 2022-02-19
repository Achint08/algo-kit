# Single Source Shortest Path Algorithm
# Dijkstra Algorithm
# Note -
# 1. It works only on graphs with no negative cycle.
# 2. Don't use it for graphs with negative weight. (Especially with undirected graph).
# Technically, a undirected graph with negative weight is a negative cycle.

import heapq


# More inclined toward greedy approach.
def dijkstra(source, vertices, adj_list):

    dist = {}
    parent = {}

    for vertice in vertices:
        dist[vertice] = float('inf')
        parent[vertice] = None

    dist[source] = 0

    priority_queue = [(0, source)]

    while(priority_queue):
        curr_dist, curr_node = heapq.heappop(priority_queue)

        # Not equal to, to avoid source not to fail first source case.
        # There is a possibility that a node be there in priority queue multiple
        # times. let's say, we added the element in queue the first time and we
        # got a better distance before we pop, in that case, the node with
        # with larger distance will just be ignored. That's what we want.
        if curr_dist > dist[curr_node]:
            continue

        for adj_node in adj_list[curr_node]:
            new_dist = curr_dist + adj_list[curr_node][adj_node]

            if dist[adj_node] > new_dist:
                dist[adj_node] = new_dist
                parent[adj_node] = curr_node
                heapq.heappush(priority_queue, (new_dist, adj_node))

    return dist, parent


adj_list = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

vertices = adj_list.keys()

print(dijkstra('U', vertices, adj_list))
