from typing import List

class Solution:
    def is_safe(self, col, row, board, n):
        # same row
        for i in range(col):
            if board[row][i] == "Q":
                return False
        # upper left diagonal
        i = row
        j = col
        while (i >= 0 and j >= 0):
            if (board[i][j] == "Q"):
                return False
            i -= 1
            j -= 1
        # lower left diagonal
        i = row
        j = col
        while (i < n and j >= 0):
            if (board[i][j] == "Q"):
                return False
            i += 1
            j -= 1
        return True

    def generate_brute(self, board, ans, n, col):
        if (col == n):
            temp = [''.join(row) for row in board]
            ans.append(temp)
            return
        for row in range(0, n):
            if (self.is_safe(col, row, board, n)):
                board[row][col] = "Q"
                self.generate_brute(board, ans, n, col+1)
                board[row][col] = "."

    def solveNQueens_brute(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.generate_brute(board, ans, n, 0)
        return ans

    def generate(self, board, ans, n, col, left_row, lower_diagonal, upper_diagonal):
        if (col == n):
            temp = [''.join(row) for row in board]
            ans.append(temp)
            return
        for row in range(0, n):
            if (left_row[row] == 0 and lower_diagonal[row+col] == 0 and upper_diagonal[n-1+col-row] == 0):
                board[row][col] = "Q"
                left_row[row] = lower_diagonal[row+col] = upper_diagonal[n-1+col-row] = 1
                self.generate(board, ans, n, col+1, left_row, lower_diagonal, upper_diagonal)
                board[row][col] = "."
                left_row[row] = lower_diagonal[row + col] = upper_diagonal[n-1+col-row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        left_row = [0] * n
        lower_diagonal = [0] * (2*n - 1)
        upper_diagonal = [0] * (2*n - 1)
        self.generate(board, ans, n, 0, left_row, lower_diagonal, upper_diagonal)
        return ans

print(Solution().solveNQueens_brute(4))
print(Solution().solveNQueens(4))