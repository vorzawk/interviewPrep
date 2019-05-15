from binaryTree import Node
# The binary searh tree definition here allows duplicates, this is not ideal coz this would make search and deletion harder. Also,
# intuitively, it makes no sense to store an identical element separately. However, modifying all the code to disallow duplicates
# seems to be a huge amount of effort!

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
    """ returns the first instance of key in the tree """
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

def insertKey(node, key):
    """ inserts key into the tree as a leaf node """
    if node is None:
        print("No tree to insert into!")
        return
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









