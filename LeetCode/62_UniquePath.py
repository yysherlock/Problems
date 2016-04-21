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

class Solution1(object):
    # Time Limit Exceeded
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.walk(m,n)

    def walk(self,m,n):
        if n==1 and m==1:
            return 1
        if m > 1 and n > 1:
            return self.walk(m-1,n) + self.walk(m,n-1) # many repeated subproblems
        elif m > 1:
            return self.walk(m-1,n)
        else: # n > 1
            return self.walk(m,n-1)
