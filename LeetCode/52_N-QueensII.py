class Solution(object):

    cnt = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # vis[0][i]: whether ith col is occupied or not, i = col
        # vis[1][i]: whether ith diag is occupied or not, i = n + col - row
        # vis[2][i]: whether ith second diag is occupied or not, i = col + row
        vis = [[0 for j in range(2*n)] for i in range(3)]
        def search(row):
            if row == n:
                self.cnt += 1
                return
            for col in range(n):
                if vis[0][col]==0 and vis[1][n+col-row]==0 and vis[2][col+row]==0:
                    vis[0][col] = vis[1][n+col-row] = vis[2][col+row] = 1
                    search(row+1)
                    vis[0][col] = vis[1][n+col-row] = vis[2][col+row] = 0

        search(0)
        return self.cnt
                    
