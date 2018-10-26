class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                if target in matrix[i]:
                    return True
                return False
        return False