from typing import List

def upperBound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] <= target):
            low = mid + 1
        elif (arr[mid] > target):
            ans = mid
            high = mid - 1
    return ans

def smaller_equal(matrix, target):
    n = len(matrix)
    cnt = 0
    for i in range(0, n):
        cnt += upperBound(matrix[i], target)
    return cnt

class Solution:
    def findMedian_optimal(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        low = min(matrix[i][0] for i in range(n))
        high = max(matrix[i][m-1] for i in range(n))
        while (low <= high):
            mid = (low + high) // 2
            small_equal = smaller_equal(matrix, mid)
            if (small_equal <= (n*m)//2):
                low = mid + 1
            else:
                high = mid - 1
        return low

print(Solution().findMedian_optimal([[1,4,9],[2,5,6],[3,8,7]]))
print(Solution().findMedian_optimal([[1,3,8],[2,3,4],[1,2,5]]))