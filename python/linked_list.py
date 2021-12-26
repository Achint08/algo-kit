class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):

        if not prev_node:
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return

        last = self.head

        while(last.next):
            last = last.next

        last.next = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while(temp):
            if temp.data == key:
                break

            prev = temp
            temp = temp.next

        if not temp:
            return
        else:
            prev.next = temp.next
            temp = None


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insert_after(llist.head.next, 8)
    print('Created linked list is:')
    llist.print_list()
    llist.delete_node(7)
    print('-')
    llist.print_list()
