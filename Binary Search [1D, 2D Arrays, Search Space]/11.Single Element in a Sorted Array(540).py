from typing import List

class Solution:
    def singleNonDuplicate_brute(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            if (i == 0):
                if (nums[i] != nums[i+1]):
                    return nums[i]
            elif (i == n-1):
                if (nums[i] != nums[i-1]):
                    return nums[i]
            else:
                if (nums[i] != nums[i-1] and nums[i] != nums[i+1]):
                    return nums[i]
        return -1

    def singleNonDuplicate_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1):
            return nums[0]
        if (nums[0] != nums[1]):
            return nums[0]
        if (nums[n-1] != nums[n-2]):
            return nums[n-1]
        low = 1
        high = n-2
        while(low <= high):
            mid = (low+high) // 2
            if (nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
                return nums[mid]
            # ele is rhs
            if (((mid % 2 == 0) and nums[mid] == nums[mid+1]) or ((mid % 2 == 1) and nums[mid] == nums[mid-1])):
                low = mid + 1
            # ele is lhs
            else:
                high = mid - 1
        return -1



print(Solution().singleNonDuplicate_brute([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate_brute([3,3,7,7,10,11,11]))
print(Solution().singleNonDuplicate_optimal([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate_optimal([3,3,7,7,10,11,11]))

