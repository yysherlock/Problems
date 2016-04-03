# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

class Solution2(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return
        inverted = TreeNode(root.val)
        inverted.left, inverted.right = self.invertTree(root.right), self.invertTree(root.left)

        return inverted

def print_tree(tree):
    if not tree:
        return
    print tree.val
    print_tree(tree.left)
    print_tree(tree.right)

sol1 = Solution1()
tree = TreeNode(1); tree.left = TreeNode(2); tree.right=TreeNode(3)
sol1.invertTree(tree)
print_tree(tree)
