from collections import deque
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def preOrderTraversal(root: Node):
    """ Traverses each node of the tree recursively, printing in the following order : root -> left -> right """
    # recursive solution for pre=order traversal, iterative solution seems much harder!
    if root is None:
        return
    print(root.value, end=' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    return

def postOrderTraversal(root: Node):
    """ Traverses the tree recursively, printing in the following order : left -> right -> root """
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value, end=' ')
    return

def inOrderTraversal(root: Node):
    """ Traverses the tree recursively, printing the values in the following order : left -> root -> right """
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.value, end=' ')
    inOrderTraversal(root.right)
    return

def levelOrderTraversal(root: Node):
    if root is None:
        return
    queue = deque([root])
    while(queue):
        curr = queue.popleft()
        print(curr.value, end=' ')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)













