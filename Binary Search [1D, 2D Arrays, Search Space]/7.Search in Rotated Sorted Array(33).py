from typing import List

class Solution:
    def normal_binary_search(self, nums: List[int], target: int) -> int:
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

    def search_index(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while (low < high):
            if (high == (low + 1)):
                return low
            mid = (low + high) // 2
            if (nums[mid] > nums[high]):
                low = mid
            elif (nums[mid] <= nums[low]):
                high = mid
            else:
                return -1
        return None

    def search_1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        index = Solution().search_index(nums)
        if ((index == None) and nums[0] == target):
            return 0
        elif ((index == None) and nums[0] != target):
            return -1
        elif (index == -1):
            presence1 = Solution().normal_binary_search(nums, target)
            if (presence1 != -1):
                return presence1
            else:
                return -1
        else:
            presence1 = Solution().normal_binary_search(nums[0:(index+1)], target)
            presence2 = Solution().normal_binary_search(nums[(index+1):n], target)
            if (presence1 != -1):
                return presence1
            elif (presence2 != -1):
                return presence2+index+1
            else:
                return -1


    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == target):
                return mid
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


print(Solution().search_1([4,5,6,7,0,1,2], 0))
print(Solution().search_1([4,5,6,7,0,1,2], 3))
print(Solution().search_1([1], 0))
print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1], 0))
print(Solution().search_1([1,2,3,4,5], 4))
