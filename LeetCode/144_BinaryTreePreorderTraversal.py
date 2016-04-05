# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


def preorderTraversal(self, root): # iteratively, without recursive
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        result = []
        stack = [root]

        while len(stack) > 0:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return result
