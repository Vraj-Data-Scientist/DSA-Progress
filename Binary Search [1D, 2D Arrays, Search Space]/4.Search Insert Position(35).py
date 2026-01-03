from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        ans = n
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] < target):
                low = mid + 1
            elif (nums[mid] >= target):
                ans = mid
                high = mid - 1
        return ans

print(Solution().searchInsert([1,3,5,6], 5))
print(Solution().searchInsert([1,3,5,6], 2))
print(Solution().searchInsert([1,3,5,6], 7))