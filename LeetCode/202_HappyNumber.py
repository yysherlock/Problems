class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set({})

        while n>0:
            if n in seen:
                return False
            seen.add(n)
            if n==1: return True
            re = 0
            while n:
                re += (n % 10)**2
                n /= 10
            n = re
        
