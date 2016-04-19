class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0: return False
        while n:
            if n==1: return True
            if n % 3: return False
            n /= 3
        return True

        
