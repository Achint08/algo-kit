# Disjoint set Find - Union using union by rank and path compression.
# The idea of union by rank and path compression is to
# reduce time complexity while doing union between two
# disjoint set. We do union in such a way that we attach shorter
# tree to a longer tree always.
#
# Disjoint set has application in cycle detection.
# The idea is to perform the following operations:
# 1. form individual sets during initialization
# 2. Performing union of sets if two elements belong to same set
# 3. Checking if two elements belong to same disjoint set.

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if size[parent_x] < size[parent_y]:
        parent[parent_x] = parent_y
        size[parent_y] += size[parent_x]
    else:
        parent[parent_y] = parent_x
        size[parent_x] += size[parent_y]


def is_same_set(x, y):
    parent_x = find(x)
    if parent_x == find(y):
        return True
    else:
        return False


if __name__ == '__main__':
    parent = [i for i in range(10)]
    size = [1 for i in range(10)]

    print(is_same_set(1, 2))
    union(1, 2)
    print(is_same_set(1, 2))
    union(2, 3)
    print(is_same_set(2, 3))
    print(is_same_set(1, 7))
