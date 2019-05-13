class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createBST(array):
    """ creates a binary search tree based on the given array of elements """
    arrLen = len(array)
    if arrLen == 0:
        print("Can't create a BST coz the array contains no elements!")
        return
    if arrLen == 1:
        return Node(array[0])
    # To create the binary tree, we first sort the array, and start creaing the tree recursively from the median.
    array.sort()
    mid = arrLen//2
    bst = Node(array[mid])
    bst.left = createBST(array[0:mid])
    if arrLen > 2:
        bst.right = createBST(array[mid+1:])
    return bst

def searchKey(node, key):
    if node is None:
        return
    if key == node.value:
        return node
    if key < node.value:
        return searchKey(node.left, key)
    if key > node.value:
        return searchKey(node.right, key)
    print("Error: something is wrong")
    return


