from collections import deque


def bfs(node):
    queue = deque()
    queue.append(node)
    # Other way is to create a dictionary and initialize it as false. Set it to true once visited
    # It should be in process, not visited, because in process will eventually be visited, unless breaked
    visited = set()
    visited.add(node)

    while(queue):
        node = queue.popleft()
        print(node)
        for next_node in adj_list.get(node, []):
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)


def add_edge(u, v):
    adj_list[u] = adj_list.get(u, []) + [v]


if __name__ == '__main__':
    adj_list = {}
    edge_set = [edge for edge in input().split(' ')]
    for edge in edge_set:
        nodes = [int(node) for node in edge.split(',')]
        add_edge(nodes[0], nodes[1])
    print(adj_list)
    bfs(7)
