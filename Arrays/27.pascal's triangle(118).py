from typing import List

class Solution:
    def ncr(self, n, r):
        ans = 1
        for i in range(0, r):
            ans = ans * (n - i)
            ans = ans // (i + 1)
        return ans
    def generate_brute(self, numRows: int) -> List[List[int]]:
        triangle = [[1 for c in range(1, r+1)] for r in range(1, numRows+1)]
        for r in range(0, numRows):
            for c in range(0, r+1):
                triangle[r][c] = Solution().ncr(r, c)
        return triangle

    def generate_better(self, numRows: int) -> List[List[int]]:
        triangle = []
        for r in range(0, numRows):
            list1 = []
            value = 1
            list1.append(1)
            for c in range(1, r+1):
                value = value * (r - c + 1) // (c)
                list1.append(value)
            triangle.append(list1)
        return triangle

    def generate_optimal(self, numRows: int) -> List[List[int]]:
        triangle = [[1 for c in range(1, r+1)] for r in range(1, numRows+1)]
        for r in range(0, numRows):
            for c in range(1, r):
                triangle[r][c] = triangle[r-1][c] + triangle[r-1][c-1]
        return triangle


print(Solution().generate_brute(5))
print(Solution().generate_brute(1))
print(Solution().generate_better(5))
print(Solution().generate_better(1))
print(Solution().generate_optimal(5))
print(Solution().generate_optimal(1))


