from typing import List

class Solution:
    def celebrity_brute(self, mat):
        n = len(mat)
        for i in range(0, n):
            knows_someone = False
            for j in range(0, n):
                if (mat[i][j] == 1):
                    knows_someone = True
            if knows_someone:
                continue
            is_celebrity = True
            for j in range(0, n):
                if (i!= j and mat[j][i] == 0):
                    is_celebrity = False
                    break
            if is_celebrity:
                return i
        return -1

    def celebrity_better(self, mat):
        n = len(mat)
        i_know = [0] * n
        know_me = [0] * n
        for i in range(0, n):
            for j in range(0, n):
                if (mat[i][j] == 1):
                    i_know[i] += 1
                    know_me[j] += 1
        for i in range(0, n):
            if (i_know[i] == 0 and know_me[i] == n-1):
                return i
        return -1

    def celebrity_optimal(self, mat):
        n = len(mat)
        top = 0
        down = n-1
        while (top < down):
            if (mat[top][down] == 1):
                top += 1
            elif (mat[down][top] == 1):
                down -= 1
            else:
                top += 1
                down -= 1
        if (top > down):
            return -1
        for i in range(0, n):
            if (i == top):
                continue
            if (mat[top][i] == 0 and mat[i][top] == 1):
                pass
            else:
                return -1
        return top

print(Solution().celebrity_brute([
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0]
    ]))
print(Solution().celebrity_better([
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0]
    ]))
print(Solution().celebrity_optimal([
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0]
    ]))

