def find(x):
    while(parent[x] != x):
        x = parent[x]

    return x


def union(x, y):
    x_parent = find(x)
    y_parent = find(y)

    if count[y_parent] > count[x_parent]:
        parent[x_parent] = y_parent
        count[y_parent] += count[x_parent]
    else:
        parent[y_parent] = x_parent
        count[x_parent] += count[y_parent]


def krushkal(edges):

    min_cost = 0
    for weight, source, destination in edges:

        if find(source) != find(destination):
            min_cost += weight
            union(source, destination)

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

    edge_list = []

    for source in adj_list:
        for destination in adj_list[source]:
            edge_list.append(
                (adj_list[source][destination], source, destination))

    edge_list.sort()
    vertices = adj_list.keys()

    count = {}
    parent = {}

    for vertice in vertices:
        count[vertice] = 1
        parent[vertice] = vertice

    print(krushkal(edge_list))
