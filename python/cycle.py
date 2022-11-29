# Classification of edges:
# Tree edge: An edge (u, v) such that v is descendant of u in the dfs-tree
# Forward edge: An edge (u, v) such that v is descendant of u but not part of dfs-tree
# Back edge - An edge (u, v) such that u is descendant of v is the dfs-tree
# Cross edge - An edge (u, v) such that u is not related to v anyway in dfs-tree. Belongs to different tree in forest.
#
# Note -
# 1. For cycle detection - check if there is any back edge
# 2. For classification between cross and forward edge:
# a. If start time of the curr node is less than the neighbouring node, this means neigbouring
# node is the descendant of curr node, therefore it is a forward edge.
# b. If start time of the curr node is more than the neighbouring node, this means neigbouring
# node can already been visited before and not a descendant for sure, therefore it is a cross edge.
# 3. Forest = Set of trees.


def dfs(node):
    global color, back_edge, curr_time, start_time, finish_time, forward_edge, cross_edge, tree_edge
    color[node] = 'grey'
    start_time[node] = curr_time
    curr_time += 1

    for neighbour in adj_list[node]:
        if color[neighbour] == 'grey':
            back_edge += 1
        elif color[neighbour] == 'white':
            tree_edge += 1
            dfs(neighbour)
        elif color[neighbour] == 'black':
            if start_time[node] < start_time[neighbour]:
                forward_edge += 1
            else:
                cross_edge += 1

    color[node] = 'black'
    finish_time[node] = curr_time
    curr_time += 1


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

    color = {}
    start_time = {}
    finish_time = {}
    curr_time = 0
    back_edge = cross_edge = forward_edge = tree_edge = 0
    for vertice in vertices:
        color[vertice] = 'white'
        start_time[vertice] = -1
        finish_time[vertice] = -1

    for vertice in vertices:
        if color[vertice] == 'white':
            dfs(vertice)

    if back_edge >= 1:
        print('Cycle detected')

    print(back_edge, forward_edge, cross_edge, tree_edge)
