from typing import List


def max_ele(arr, col):
    n = len(arr)
    max_val = float('-inf')
    index = -1
    for i in range(n):
        if arr[i][col] > max_val:
            max_val = arr[i][col]
            index = i
    return index

class Solution:
    def findPeakGrid_optimal(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while (low <= high):
            mid = (low + high) // 2
            row = max_ele(mat, mid)
            left = mat[row][mid-1] if mid-1 >= 0 else float('-inf')
            right = mat[row][mid+1] if mid+1 < m else float('-inf')
            if (mat[row][mid] > left and mat[row][mid] > right):
                return [row, mid]
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]

print(Solution().findPeakGrid_optimal([[10,20,15],[21,30,14],[7,16,32]]))
print(Solution().findPeakGrid_optimal([[1,4],[3,2]]))