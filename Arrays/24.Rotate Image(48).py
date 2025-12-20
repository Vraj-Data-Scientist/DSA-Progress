from typing import List

class Solution:
    def rotate_brute(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                ans[j][n-1-i] = matrix[i][j]
        return ans

    def reverse(self, matrix, i, left, right):
        while (left < right):
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
    def rotate_optimal(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n-1):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0, n):
            Solution().reverse(matrix, i, 0, (m-1))
        return matrix






print(Solution().rotate_brute([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().rotate_brute([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(Solution().rotate_optimal([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().rotate_optimal([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

