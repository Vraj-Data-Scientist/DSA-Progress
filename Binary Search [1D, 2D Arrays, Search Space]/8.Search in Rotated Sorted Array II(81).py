from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == target):
                return True
            if (nums[low] == nums[mid] and nums[mid] == nums[high]):
                low = low + 1
                high = high - 1
                continue
            # left sorted
            if (nums[mid] >= nums[low]):
                if (target < nums[mid] and nums[low] <= target):
                    high = mid - 1
                else:
                    low = mid + 1
            # right sorted
            elif (nums[mid] <= nums[high]):
                if (target > nums[mid] and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1



print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1], 0))
print(Solution().search([3,3,3,4,3,3], 4))
print(Solution().search([3,3,3,0,3,3], 4))
