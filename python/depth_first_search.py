# Visited can be maintained centrally to visited all components of graph
# def dfs_iterative(node):
#     stack = []
#     visited = set()
#     stack.append(node)
#     visited.add(node)
#     while(stack):
#         node = stack.pop()
#         print(node)
#         for next_node in adj_list.get(node, []):
#             if next_node not in visited:
#                 stack.append(next_node)
#                 visited.add(next_node)

# Color logic doesn't work in dfs iterative
def dfs_recursive(node):
    print(node)
    color[node] = 'gray'
    for next_node in adj_list.get(node, []):
        if color[next_node] == 'white':
            dfs_recursive(next_node)

    color[node] = 'black'


def add_edge(u, v):
    adj_list[u] = adj_list.get(u, []) + [v]
    # For undirected graph
    # adj_list[v] = adj_list.get(v, []) + [u]


if __name__ == '__main__':
    adj_list = {}
    inp = "1,2 2,3 2,4 4,6 4,1 4,5 7,8"
    # edge_set = [edge for edge in input().split(' ')]
    edge_set = [edge for edge in inp.split(' ')]
    color = {}
    for edge in edge_set:
        nodes = [int(node) for node in edge.split(',')]
        add_edge(nodes[0], nodes[1])
        color[nodes[0]] = color[nodes[1]] = 'white'
    print(adj_list)
    # dfs_iterative(1)
    dfs_recursive(1)
