# Topological sort, basically sorts vertices in a manner, such that,
# if u comes before v, then either it's not connected, or if its' connected in graph,
# there is an edge from u to v.
# Key points -
#
# Topological sort works only on Directed Acyclic Graph(DAG).

def dfs_util(node):
    global color, finished

    color[node] = 'grey'
    for neighbour in adj_list[node]:
        if color[neighbour] == 'white':
            dfs_util(neighbour)
    color[node] = 'black'
    finished.append(node)


if __name__ == '__main__':
    adj_list = {'a': {'b': 1, 'd': 1}, 'b': {'c': 1}, 'd': {
        'e': 1}, 'c': {'e': 1, 'd': 1}, 'f': {}, 'e': {}}
    vertices = adj_list.keys()
    color = {}
    for vertice in vertices:
        color[vertice] = 'white'

    finished = []
    for vertice in vertices:
        if color[vertice] == 'white':
            dfs_util(vertice)

    print(finished)
