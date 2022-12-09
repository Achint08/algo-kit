# Binary Search Tree is a binary tree with following properties for each node in the tree:
# 1. The left subtree has keys less than the current node
# 2. The right subtree has keys more than the current node
# 3. There are no duplicate nodes.

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search(root, key):
    if not root or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


def insert(root, key):
    if not root:
        return Node(key)

    if root.val < key:
        root.right = insert(root.right, key)
    elif root.val > key:
        root.left = insert(root.left, key)

    return root


def find_successor(root):
    curr = root.right

    while(curr.left):
        curr = curr.left

    return curr


def delete(root, key):
    if not root:
        return root

    if root.val < key:
        root.right = delete(root.right, key)
    elif root.val > key:
        root.left = delete(root.left, key)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            temp = root.right
            root.right = None
            return temp

        elif not root.right:
            temp = root.left
            root.left = None
            return temp
        else:
            successor = find_successor(root)
            root.val = successor.val
            delete(root.right, successor.val)
            return root


if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    print(search(r, 46) == None)
    print(search(r, 60) == None)
    print(delete(r, 70))
