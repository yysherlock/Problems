class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        n = [2,3,5]
        if num<=0: return False
        if num==1: return True
        for i in range(1, int(math.sqrt(num))+1):
            if num % i == 0: # i is factor
                # For each prime factor i, if i not in [2,3,5], not ugly, False
                if self.isPrime(i) and (i not in n): return False
                if self.isPrime(num/i) and (num/i not in n): return False

        return True

    def isPrime(self,num):
        import math
        if num==1: return False
        flag = True
        for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0: # i is not prime
                flag = False
                break
        return flag
