# def add_edge_weighted(u, v, w):
#     adj_matrix[u - 1][v - 1] = w
#     # For undirected graph,
#     # adj_matrix[v - 1][u - 1] = w


def add_edge(u, v):
    adj_matrix[u - 1][v - 1] = 1
    # For undirected graph,
    # adj_matrix[v - 1][u - 1] = 1


if __name__ == '__main__':
    nodes = int(input())
    adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
    edge_set = [edge for edge in input().split(' ')]
    for edge in edge_set:
        nodes = [int(node) for node in edge.split(',')]
        add_edge(nodes[0], nodes[1])
    print(adj_matrix)
