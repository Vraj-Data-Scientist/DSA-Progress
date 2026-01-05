from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        low = 0
        high = n-1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[low] <= nums[mid] and nums[mid] < nums[high]):
                ans = min(ans, nums[low])
                break
            # left sorted
            if (nums[low] <= nums[mid]):
                ans = min(ans, nums[low])
                low = mid + 1
            # right sorted
            elif (nums[mid] < nums[high]):
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans

print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([4,5,6,7,0,1,2]))

