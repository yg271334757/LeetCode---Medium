class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        num_r, num_c = len(board), len(board[0])
        return any(self.dfs(board, word, 0, r, c) for r in range(num_r)
                                                  for c in range(num_c))

    def dfs(self, board, word, ndx, r, c):
        if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c] != word[ndx]:
            return False
        if ndx == len(word)-1:
            return True

        board[r][c] = "*" # mark current position as visited using *
        result = False
        result = self.dfs(board, word, ndx+1, r-1, c) or\
                 self.dfs(board, word, ndx+1, r+1, c) or\
                 self.dfs(board, word, ndx+1, r, c-1) or\
                 self.dfs(board, word, ndx+1, r, c+1)
        board[r][c] = word[ndx] # backtrack
        return result