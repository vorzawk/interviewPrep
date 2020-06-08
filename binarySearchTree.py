from binaryTree import Node, inOrderTraversal
# The binary searh tree definition here allows duplicates, this is a feature not a bug.

class BST:
    def __init__(self, array):
        def createBST(array):
            """ initializes a binary search tree based on the given array of elements """
            numElems = len(array)
            if numElems == 0:
                return None
            if numElems == 1:
                return Node(array[0])
            # To create the binary search tree, we first sort the array, and start creaing the tree recursively from the median.
            array.sort()
            mid = numElems // 2
            root = Node(array[mid])
            root.left = createBST(array[0:mid])
            root.right = createBST(array[mid+1:])
            return root
        self.root = createBST(array)

def search(self, key):
    def searchKey(node, key):
        """ returns the first instance of key in the tree """
        if node is None:
            return
        if key == node.value:
            return node
        if key < node.value:
            return searchKey(node.left, key)
        if key > node.value:
            return searchKey(node.right, key)
        print("Error: We should have never reached this point")
        return
    return searchKey(self.root, key)

def insert(self, key):
    def insertKey(node, key):
        """ inserts key into the tree as a leaf node """
        if key <= node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                insertKey(node.left, key)
        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                insertKey(node.right, key)
        return
    if self.root is None:
        self.root = Node(key)
        return
    insertKey(self.root, key)


def delete(self, key):
    def deleteKey(node, key):
        """ deletes the first instance of key from the tree and returns the new tree """
        if node is None:
            return
        if node.value == key:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # If the control reaches here, then the node to be deleted has 2 children
            # We need to find the least element in the right subtree and use it to replace the value to be deleted.
            currNode = node.right
            while currNode.left:
                currNode = currNode.left
            minVal = currNode.value
            node.right = deleteKey(node.right, minVal)
            node.value = minVal
            return node
        elif node.value < key:
            node.right = deleteKey(node.right, key)
        elif node.value > key:
            node.left = deleteKey(node.left, key)
        return node
    self.root = deleteKey(self.root, key)











