class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        r = len(board)
        c = len(board[0])
        def dfs(board, y, x):
            if x < 0 or x >= c or y < 0 or y >= r or board[y][x] != 'O':
                return 
            board[y][x] = 'S'
            dfs(board, y + 1, x)
            dfs(board, y - 1, x)
            dfs(board, y, x + 1)
            dfs(board, y, x - 1)
        for i in range(c):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[r-1][i] == 'O':
                dfs(board, r-1, i)
        for j in range(r):
            if board[j][0] == 'O':
                dfs(board, j, 0)
            if board[j][c-1] == 'O':
                dfs(board, j, c-1)
        for y in range(r):
            for x in range(c):
                if board[y][x] == 'S':
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'
        