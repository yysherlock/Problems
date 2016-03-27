# Calculate sum of even layers (evensum) and sum of odd layers(oddsum) of the tree, then obtain max(evensum, oddsum)
# But this is wrong for 337 problem.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def __init__(self):
        self.evensum = 0
        self.oddsum = 0
    
    def dfs(self, root, curlayer):
        if curlayer % 2 == 0: self.evensum += root.val
        else: self.oddsum += root.val
        if root.left: 
            self.dfs(root.left, curlayer + 1)
        if root.right: 
            self.dfs(root.right, curlayer + 1)
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs
        if root:
            self.dfs(root, 0)
        return max(self.evensum, self.oddsum)
        
