from typing import List
class Solution:
    def mark_row(self, i:int, matrix:List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        for j in range(0, m):
            if (matrix[i][j] != 0):
                matrix[i][j] = None
    def mark_col(self, j:int, matrix:List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            if (matrix[i][j] != 0):
                matrix[i][j] = None
    def setZeroes_brute(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            for j in range(0, m):
                if (matrix[i][j] == 0):
                    Solution().mark_row(i, matrix)
                    Solution().mark_col(j, matrix)
        for i in range(0, n):
            for j in range(0, m):
                if (matrix[i][j] == None):
                    matrix[i][j] = 0
        return matrix

    def setZeroes_better(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row_p = [0]*n
        col_p = [0]*m
        for i in range(0, n):
            for j in range(0, m):
                if (matrix[i][j] == 0):
                    row_p[i] = 1
                    col_p[j] = 1
        for i in range(0, n):
            for j in range(0, m):
                if (row_p[i] or col_p[j]):
                    matrix[i][j] = 0
        return matrix

    def setZeroes_optimal(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        col_0 = 1
        for i in range(0, n):
            for j in range(0, m):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    if (j != 0):
                        matrix[0][j] = 0
                    else:
                        col_0 = 0
        for i in range(1, n):
            for j in range(1, m):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
        if (matrix[0][0] == 0):
            for j in range(0, m):
                matrix[0][j] = 0
        if (col_0 == 0):
            for i in range(0, n):
                matrix[i][0] = 0
        return matrix



print(Solution().setZeroes_brute([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(Solution().setZeroes_brute([[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().setZeroes_better([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(Solution().setZeroes_better([[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().setZeroes_optimal([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(Solution().setZeroes_optimal([[1,1,1],[1,0,1],[1,1,1]]))



