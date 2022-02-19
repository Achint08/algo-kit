from collections import deque


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Application:
# 1. Gives element in non-decreasing order


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# Application:
# 1. To copy the tree.
# 2. To get prefix of expression tree


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


# Application:
# 1. To delete the tree.
# 2. To get postfix of expression tree


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


# Specs: Unlike all traversal above, it doesn't follow DFS
# Application:
# 1. To perform some operation in level order

def levelorder(root):
    queue = deque()
    queue.append(root)
    while(queue):
        node = queue.popleft()

        print(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('In order')
    inorder(root)
    print('Pre order')
    preorder(root)
    print('Post order')
    postorder(root)
    print('Level order')
    levelorder(root)
