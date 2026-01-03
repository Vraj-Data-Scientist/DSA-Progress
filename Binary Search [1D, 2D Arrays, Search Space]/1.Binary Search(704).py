from typing import List

class Solution:
    def search_iterative(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while (low <= high):
            mid = (low + high) // 2
            if (target < nums[mid]):
                high = mid - 1
            elif (target > nums[mid]):
                low = mid + 1
            else:
                return mid
        return -1

    def search_recursive(self, nums: List[int], target: int, low:int, high:int) -> int:
        if high is None:
            high = len(nums)-1
        if (low > high):
            return -1
        mid = (low + high) // 2
        if (target < nums[mid]):
            return Solution().search_recursive(nums, target, low, mid-1)
        elif (target > nums[mid]):
            return Solution().search_recursive(nums, target, mid+1, high)
        else:
            return mid



print(Solution().search_iterative([-1,0,3,5,9,12], 9))
print(Solution().search_iterative([-1,0,3,5,9,12], 2))
print(Solution().search_recursive([-1,0,3,5,9,12], 9, 0, None))
print(Solution().search_recursive([-1,0,3,5,9,12], 2, 0, None))