class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c-1, -1, -1):
                if matrix[i][j] < target:
                    break
                elif matrix[i][j] == target:
                    return True
        return False