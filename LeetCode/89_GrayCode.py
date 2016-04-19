class Solution(object):
    re = []
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        vis = [0 for i in range(1<<n)]
        vis[0] = 1
        if self.generate(vis, [0], 0, n):
            return self.re


    def generate(self,vis,re,cur,n):
        if len(re)==(1<<n):
            self.re = re
            return 1
        for i in range(n):
            cur ^= 1<<i # flip ith bit of cur
            if not vis[cur]:
                vis[cur] = 1
                if self.generate(vis,re+[cur],cur,n): return 1
                vis[cur] = 0
            cur ^= 1<<i

class Solution1(object):
    re = []

    def grayCode(self, n):

        vis = [0 for i in range(1<<n)]
        vis[0] = 1
        self.generate(vis, [0], 0, n)

    def generate(self,vis,re,cur,n):
        if len(re)==(1<<n):
            print re
            return
        for i in range(n):
            cur ^= 1<<i # flip ith bit of cur
            if not vis[cur]:
                vis[cur] = 1
                self.generate(vis,re+[cur],cur,n)
                vis[cur] = 0
            cur ^= 1<<i


#sol = Solution()
#print sol.grayCode(2)

sol1 = Solution1()
sol1.grayCode(3)
