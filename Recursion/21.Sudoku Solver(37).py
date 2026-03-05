from typing import List

class Solution:
    def __init__(self):
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

    def is_valid_brute(self, board, row, col, c):
        for i in range(9):
            # in that col
            if board[i][col] == c:
                return False
            # in that row
            if board[row][i] == c:
                return False
            # in that box
            box_row_start = 3 * (row // 3)
            box_col_start = 3 * (col // 3)
            if board[box_row_start + (i//3)][box_col_start + (i%3)] == c:
                return False
        return True

    def solveSudoku_brute(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if (board[i][j] == "."):
                    for c in map(str, range(1,10)):
                        if (self.is_valid_brute(board, i, j, c)):
                            board[i][j] = c
                            if (self.solveSudoku_brute(board) == True):
                                return True
                            # don't come here if already true---it avoids
                            board[i][j] = "."
                    return False
        return True

    def ans(self, board):
        self.solveSudoku_brute(board)
        print(board)

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(Solution().ans(board))
