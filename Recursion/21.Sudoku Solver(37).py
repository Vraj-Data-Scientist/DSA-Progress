from typing import List

class Solution:
    def __init__(self):
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.empties = []

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

    def ans_brute(self, board):
        self.solveSudoku_brute(board)
        print(board)

    def helper(self, board):
        self.empties = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    box = (i // 3) * 3 + (j // 3)
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[box].add(num)
                else:
                    self.empties.append((i,j))
        # print(self.rows)
        # print(self.cols)
        # print(self.boxes)
        self.solveSudoku(board, 0)

    def solveSudoku(self, board, pos):
        # all empty cells filled
        if pos == len(self.empties):
            return True
        r, c = self.empties[pos]
        box = (r // 3) * 3 + (c // 3)
        for ch in map(str, range(1, 10)):
            if (ch not in self.rows[r] and
                ch not in self.cols[c] and
                ch not in self.boxes[box]):
                board[r][c] = ch
                self.rows[r].add(ch)
                self.cols[c].add(ch)
                self.boxes[box].add(ch)
                if (self.solveSudoku(board, pos+1) == True):
                    return True
                board[r][c] = "."
                self.rows[r].remove(ch)
                self.cols[c].remove(ch)
                self.boxes[box].remove(ch)
        return False

    def ans(self, board):
        self.helper(board)
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
print(Solution().ans_brute(board))
board2 = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(Solution().ans(board2))
