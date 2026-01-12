from typing import List

def binary_search(nums: List[int], target: int) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    while (low <= high):
        mid = (low + high) // 2
        if (target < nums[mid]):
            high = mid - 1
        elif (target > nums[mid]):
            low = mid + 1
        else:
            return mid
    return -1

class Solution:
    def searchMatrix_brute(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            for j in range(0, m):
                if (matrix[i][j] == target):
                    return True
        return False

    def searchMatrix_better_1(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            ind = binary_search(matrix[i], target)
            if (ind != -1):
                return True
        return False

    def searchMatrix_better_2(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            if (matrix[i][0] <= target and target <= matrix[i][m-1]):
                ind = binary_search(matrix[i], target)
                if (ind != -1):
                    return True
        return False

    def searchMatrix_optimal(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n*m-1
        while (low <= high):
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                low = mid + 1
            else:
                high = mid - 1
        return False


print(Solution().searchMatrix_brute([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Solution().searchMatrix_brute([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(Solution().searchMatrix_better_1([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Solution().searchMatrix_better_1([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(Solution().searchMatrix_better_2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Solution().searchMatrix_better_2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(Solution().searchMatrix_optimal([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Solution().searchMatrix_optimal([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))