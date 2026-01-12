from typing import List

def lower_bound(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = (low + high) // 2
        if (nums[mid] >= target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

class Solution:
    def row_with_max_1s_brute(self, matrix, n, m):
        max_one = -1
        row_ind = -1
        for i in range(0, n):
            cnt_row = 0
            for j in range(0, m):
                cnt_row += matrix[i][j]
            if (cnt_row > max_one):
                max_one = cnt_row
                row_ind = i
        return row_ind

    def row_with_max_1s_optimal(self, matrix, n, m):
        max_one = 0
        row_ind = -1
        for i in range(0, n):
            cnt_row = m - lower_bound(matrix[i], 1)
            if (cnt_row > max_one):
                max_one = cnt_row
                row_ind = i
        return row_ind


print(Solution().row_with_max_1s_brute([[1,1,1], [0,0,1], [0,0,0]], 3, 3))
print(Solution().row_with_max_1s_brute([[0,1,1], [0,0,1], [1,1,1]], 3, 3))
print(Solution().row_with_max_1s_optimal([[1,1,1], [0,0,1], [0,0,0]], 3, 3))
print(Solution().row_with_max_1s_optimal([[0,1,1], [0,0,1], [1,1,1]], 3, 3))