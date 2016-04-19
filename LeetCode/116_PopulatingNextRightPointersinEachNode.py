# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        from collections import deque
        if not root: return
        cnt = 0 # 0th layer
        # ith layer: nodes of 0 - ith layers: idx from 1 - 2^(i+1)
        q = deque([root])
        limit = 2
        pre = None
        while len(q):
            cur = q.popleft()
            cnt += 1
            if cnt == limit:
                limit <<= 1
            elif pre: pre.next = cur
            pre = cur
            if cur.left:
                q.append(cur.left)
                q.append(cur.right)
