class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1: return True
        cur = 1
        while cur < n:
            cur <<= 1
        if cur == n: return True
        else: return False
