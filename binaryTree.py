class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def preOrderTraversal(root: TreeNode):
    """ Traverses each node of the tree recursively, printing in the following order : root -> left -> right """
    # recursive solution for pre=order traversal, iterative solution seems much harder!
    if root is None:
        return
    print(root.value)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    return

def postOrderTraversal(root: TreeNode):
    """ Traverses the tree recursively, printing in the following order : left -> right -> root """
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value)
    return

def inOrderTraversal(root: TreeNode):
    """ Traverses the tree recursively, printing the values in the following order : left -> root -> right """
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.value)
    inOrderTraversal(root.right)
    return




