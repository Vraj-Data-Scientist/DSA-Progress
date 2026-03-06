from typing import List

class Solution:
    def solve(self, i, j, idx, board, word):
        rows = len(board)
        cols = len(board[0])
        if (idx == len(word)):
            return True
        if (i >= rows or i < 0 or j >= cols or j < 0 or board[i][j] != word[idx]):
            return False
        temp = board[i][j]
        board[i][j] = "$"
        if (self.solve(i+1, j, idx+1, board, word) or
            self.solve(i-1, j, idx+1, board, word) or
            self.solve(i, j+1, idx+1, board, word) or
            self.solve(i, j-1, idx+1, board, word)):
            return True
        board[i][j] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if self.solve(i, j, 0, board, word):
                    return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCX"))