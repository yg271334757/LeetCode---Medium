class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        pos0 = 101
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(n):
            for j in range(m):
                if i == 0 and obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0 and obstacleGrid[i][j] != 0:
                    obstacleGrid[i][j:] = [0] * (m-j)
                    break
                elif (j == 0 and obstacleGrid[i][j] != 0) or (j==0 and i > pos0):
                    obstacleGrid[i][j] = 0
                    pos0 = i
                elif j == 0 and obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]