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

    def push(self, new_value):
        new_node = Node(new_value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, new_value):
        if self.head is None:
            new_node = Node(new_value)
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            self.insertAfter(node, new_value)

    def delete(self, key):
        """ delete the first instance of "key" from the linked list"""
        if self.head is None:
            return
        if self.head.value == key:
            self.head = self.head.next
        previous_node = self.head
        current_node = self.head
        while current_node and current_node.value != key:
            previous_node = current_node
            current_node = current_node.next
        if current_node:
            previous_node.next = current_node.next



