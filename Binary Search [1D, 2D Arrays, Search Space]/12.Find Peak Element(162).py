from typing import List

class Solution:
    def findPeakElement_brute(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            if (((nums[i] > nums[i-1]) or i == 0) and (i == n-1 or (nums[i] > nums[i+1]))):
                return i
        return -1

    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1):
            return 0
        if (nums[0] > nums[1]):
            return 0
        if (nums[n-1] > nums[n-2]):
            return n-1
        low = 1
        high = n - 2
        while(low <= high):
            mid = (low+high) // 2
            if (nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]):
                return mid
            elif (nums[mid] > nums[mid - 1]):
                low = mid + 1
            elif (nums[mid] > nums[mid + 1]):
                high = mid - 1
            else:
                high = mid - 1
        return -1

print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElement([1,2,1,3,5,6,4]))
print(Solution().findPeakElement_brute([1,2,3,1]))
print(Solution().findPeakElement_brute([1,2,1,3,5,6,4]))
