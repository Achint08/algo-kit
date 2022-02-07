# # For weighted graph
# def add_edge(u, v, w):
#     edge_list.append((u, v, w))
#     # For undirected graph,
#     edge_list.append((v, u, w))


def add_edge(u, v):
    edge_list.append((u, v))
    # For undirected graph,
    edge_list.append((v, u))


if __name__ == '__main__':
    nodes = int(input())
    edge_list = []
    adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
    edge_set = [edge for edge in input().split(' ')]
    for edge in edge_set:
        nodes = [int(node) for node in edge.split(',')]
        add_edge(nodes[0], nodes[1])
    print(adj_matrix)
