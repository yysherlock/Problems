class Solution(object):
    result = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.generate([],1,k,n)
        return self.result

    def generate(self,re,pos,k,n):
        if len(re)==k:
            if sum(re) == n: self.result.append(re)
            return
        for i in range(pos,10):
            self.generate(re+[i],i+1,k,n)
            
