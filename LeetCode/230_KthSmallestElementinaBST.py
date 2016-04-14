
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    # same as inorder traverse
    stack = []

    while True:
        # go to the leftmost (smallest element)
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop(-1)
        k-= 1
        if not k: return root.val
        
        while not root.right:
            root = stack.pop(-1)
            k-= 1
            if not k: return root.val
        else:
            root = root.right
# construct a tree
tree = TreeNode(2); tree.left = TreeNode(1); tree.right = TreeNode(3)
print kthSmallest(tree,3)
