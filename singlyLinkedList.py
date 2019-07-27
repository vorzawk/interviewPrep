class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def insertAfter(self, node, new_value):
        new_node = Node(new_value)
        new_node.next = node.next
        node.next = new_node

