''' # my first solution is TLE
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs (x, y):
            if x == 1 or y == 1:
                return 1
            else:
                return dfs(x-1, y) + dfs(x, y-1)
        return dfs(m,n)
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = [[[0] for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    a[i][j] = 1
                else:
                    a[i][j] = a[i-1][j] + a[i][j-1]
        return a[n-1][m-1]