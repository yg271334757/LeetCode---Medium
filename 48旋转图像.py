class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        for i in range(r//2): # 将矩阵底部和顶部互换
            for j in range(r):
                matrix[i][j], matrix[r-i-1][j] = matrix[r-i-1][j], matrix[i][j]
        for i in range(r): # 将矩阵对角线元素互换
            for j in range(i,r):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]