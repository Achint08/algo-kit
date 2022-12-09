class Node:

    def __init__(self, prev=None, next=None, data=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, new_data, prev_node):
        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(data=new_data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node
        new_node.prev = last

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return

        while(temp):
            if temp.data == key:
                break
            temp = temp.next

        if not temp:
            return

        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        temp = None


if __name__ == '__main__':

    dll = DoublyLinkedList()
    dll.push(2)
    dll.push(7)
    dll.push(8)
    dll.push(10)
    dll.append(4)
    dll.insert_after(3, dll.head.next)
    dll.print_list()
    dll.delete_node(10)
    print('-')
    dll.print_list()
