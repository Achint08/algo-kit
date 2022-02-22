import heapq


def prim(adj_list, vertices, source):

    visited = set()
    min_cost = 0
    priority_queue = []

    for destination in adj_list[source]:
        heapq.heappush(
            priority_queue,
            (adj_list[source][destination], destination)
        )

    visited.add(source)

    while(len(visited) < len(vertices)):

        weight, source = heapq.heappop(priority_queue)

        if source in visited:
            continue

        min_cost += weight
        visited.add(source)

        for destination in adj_list[source]:

            heapq.heappush(
                priority_queue, (adj_list[source][destination], destination))

    return min_cost


if __name__ == '__main__':

    adj_list = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }

    vertices = adj_list.keys()

    print(prim(adj_list, vertices, source='U'))
