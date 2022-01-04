class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)

        node.next = self.head

        if self.head:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = node
        else:
            node.next = node

        self.head = node

    def print_list(self):
        temp = self.head

        while(temp.next != self.head):
            print(temp.val)
            temp = temp.next

        print(temp.val)


if __name__ == '__main__':
    llist = CircularLinkedList()
    llist.push(6)
    llist.push(7)
    llist.push(1)
    llist.print_list()
