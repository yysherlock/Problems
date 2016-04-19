class Solution(object):
    """ Time Limit Exceeded """
    cnt = 0
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.walk(1,1,m,n)
        return self.cnt

    def walk(self,curx,cury,m,n):
        if curx==n and cury==m:
            self.cnt += 1
            return
        if curx < n: # go right
            self.walk(curx+1,cury,m,n)
        if cury < m: # go down
            self.walk(curx,cury+1,m,n)
