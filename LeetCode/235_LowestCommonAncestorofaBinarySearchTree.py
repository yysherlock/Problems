# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        import copy
        parent = {}
        parent[root] = None
        stack = [root]
        #visited = set({}) # actually, trees don't need this
        path = [root.val]
        pfound,qfound = False,False
        while len(stack) > 0 and (not pfound or not qfound):
            cur = stack.pop(-1)
            if cur==p:
                pfound = True
            if cur==q:
                qfound = True
            if cur.right:
                stack.append(cur.right)
                parent[cur.right] = cur
            if cur.left:
                stack.append(cur.left)
                parent[cur.left] = cur


        p_path = []
        cur = p
        # construct p_path
        while cur:
            p_path.append(cur)
            cur = parent[cur]
        cur = q
        while cur:
            if cur in p_path: return cur
            cur = parent[cur]


        
