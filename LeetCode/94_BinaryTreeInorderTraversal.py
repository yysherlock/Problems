# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    stack = []

    while root:
        stack.append(root)
        root = root.left

        while not root:
            if len(stack)==0: return result
            root = stack.pop() # root is leftmost node
            result.append(root.val) # add leftmost val
            root = root.right

    return result
