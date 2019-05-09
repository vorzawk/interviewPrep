class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """ Inserts a new node in front of the list """
        new_node = Node(new_data)
        new_node.next = self.head
        # If the list is empty, then the new node is the only node in the list after the push operation. So, both prev and next pointers of
        # the node are None.
        if self.head == None:
            new_node.next = None
            new_node.prev = None
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
        self.head = new_node

    def print(self):
        """Prints all elements in the list"""
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insertAfter(self, node, new_data):
        """ inserts a a node with new_data after "node" in the list """
        if node == None:
            print("Nothing to insert")
            return
        new_node = Node(new_data)
        new_node.prev = node
        #if node is the last node in the linked list, then the new node is the last after this operation.
        new_node.next = node.next
        if node.next != None:
            node.next.prev = new_node
        node.next = new_node

    def deleteNode(self, node):
        """ delete the given node from the list """
        if node is None:
            print("Nothing to delete")
            return
        # If the given node is the first node in the list, then the head should point to the next node after deletion.
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        # If the given node is the last node in the the list, then there is no prev pointer to update.
        if node.next is not None:
            node.next.prev = node.prev

    def append(self, new_data):
        """ append a new node at the end of the linked list """
        # If the list is empty, then add the new node at the start of the list.
        if self.head is None:
            self.push(new_data)
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        # now curr is the last node in the list, so we can insert the new node after it.
        self.insertAfter(curr, new_data)

    def delete(self, key):
        """ delete the first instance of key in the linked list """
        curr = self.head
        while curr is not None:
            if curr.data == key:
                self.deleteNode(curr)
                return
            curr = curr.next
        print("Deletion unsuccessful : No node exists with the given key value in the list")


