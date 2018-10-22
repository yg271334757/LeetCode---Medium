class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):                
                if board[i][j] == '.': continue
                x = int(board[i][j])                                
                if x < 1 or x > 9 or x in row_set[i] or x in col_set[j] or x in box_set[i//3][j//3]: return False
                row_set[i].add(x)
                col_set[j].add(x)
                box_set[i//3][j//3].add(x)                
        return True