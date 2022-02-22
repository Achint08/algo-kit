# Strongly connected graph is a graph which has path from every vertex
# to the other.
# For example, a sink vertex is a SCC in itself.


def dfs_util(node):
    global color, ft, finish_time
    color[node] = 'grey'
    for neighbour in adj_list[node]:
        if color[neighbour] == 'white':
            dfs_util(neighbour)

    color[node] = 'black'
    finish_time.append((ft, node))
    ft += 1


def get_transpose_graph(adj_list):
    transpose_adj_list = {}

    for source in adj_list:
        for destination in adj_list[source]:
            if not destination in transpose_adj_list:
                transpose_adj_list[destination] = {}
            transpose_adj_list[destination][source] = adj_list[source][destination]

    return transpose_adj_list


if __name__ == '__main__':
    adj_list = {
        '0': {'2': 1, '3': 1},
        '1': {'0': 1},
        '2': {'1': 1},
        '3': {'4': 1},
        '4': {}
    }
    vertices = adj_list.keys()
    color = {}
    finish_time = []
    for vertice in vertices:
        color[vertice] = 'white'

    ft = 0

    for vertice in vertices:
        if color[vertice] == 'white':
            dfs_util(vertice)

    adj_list = get_transpose_graph(adj_list)

    total_scc = 0
    finish_time.sort(reverse=True)

    for vertice in vertices:
        color[vertice] = 'white'

    for _, vertice in finish_time:
        if color[vertice] == 'white':
            dfs_util(vertice)
            total_scc += 1

    print(total_scc)
