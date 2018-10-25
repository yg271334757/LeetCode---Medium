class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_row = False
        first_col = False
        m = len(matrix)
        n = len(matrix[0])
        # 第一列若有0，first_col = True
        for i in range(m): 
            if matrix[i][0] == 0:
                first_col = True
        # 第一行若有0，first_row = True
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
        # 若中间有0，同时映射到首行首列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 然后通过首行首列，将所有改为0的置为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # 最后再把保存好的首行首列是否改为0的信息拿出来置为0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0