# A binary tree is tree, in which each node has at most 2 children.
# From the definition of tree, it is a graph with no cycle.
# Root -> A node with no parent.
# Leaf -> A node with no children.
# Properties: (Not important!!!!!!!)
# 1. The maximum number of nodes at level ‘l’ of a binary tree is 2^l.
# 2. The maximum number of nodes in a binary tree of height ‘h’ is 2^h – 1. Height of root = 1
# 3. In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is Log (N+1).
# 4. A Binary Tree with L leaves has at least | Log L |+ 1   levels.
# 5. In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children.
# Types of Binary tree(Not important!!!!)
# 1. Complete Tree - If all the levels are completely
# filled except possibly the last level and the last level has all keys as left as possible
# 2. Full Tree - If every node has 0 or 2 children.
# 3. Perfect Tree - All the internal nodes have two children and all leaf nodes are at the same level.

# Note:
# 1. Always remember that accessing the node will return the memory reference. So access the value.
# 2. But always remember to check if there is Node before accessing the value.

class Node:

    def __init__(self, val):
        # Generally, we don't store reference to parent, but we could if question demands
        self.val = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    if root:
        print(root.val)
    else:
        print(None)
    if root.left:
        print(root.left.val)
    else:
        print(None)
    if root.right:
        print(root.right.val)
    else:
        print(None)
    if root.left.right:
        print(root.left.right.val)
    else:
        print(None)
    if root.right.left:
        print(root.right.left.val)
    else:
        print(None)
