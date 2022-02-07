# def add_edge_weighted(u, v, w):
#     adj_list[u] = adj_list.get(u, []) + [(v, w)]
#     # For undirected graph
#     # adj_list[v] = adj_list.get(v, []) + [(u, w)]


def add_edge(u, v):
    adj_list[u] = adj_list.get(u, []) + [v]
    # For undirected graph
    # adj_list[v] = adj_list.get(v, []) + [u]


if __name__ == '__main__':
    adj_list = {}
    edge_set = [edge for edge in input().split(' ')]
    for edge in edge_set:
        nodes = [int(node) for node in edge.split(',')]
        add_edge(nodes[0], nodes[1])
    print(adj_list)
