# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        d1,d2 = 0,0
        if root.left: d1 = self.maxDepth(root.left)
        if root.right: d2 = self.maxDepth(root.right)
        return 1 + max(d1,d2)
