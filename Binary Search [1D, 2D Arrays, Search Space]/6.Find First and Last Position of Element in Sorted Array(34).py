from typing import List

def first(nums:List[int], target:int) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    first = -1
    while (low <= high):
        mid = (low + high) // 2
        if (target < nums[mid]):
            high = mid - 1
        elif (target > nums[mid]):
            low = mid + 1
        else:
            first = mid
            high = mid - 1
    return first

def last(nums:List[int], target:int) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    last = -1
    while (low <= high):
        mid = (low + high) // 2
        if (target < nums[mid]):
            high = mid - 1
        elif (target > nums[mid]):
            low = mid + 1
        else:
            last = mid
            low = mid + 1
    return last

def lowerBound(nums:List[int], target:int) -> int:
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

def upperBound(nums:List[int], target:int) -> int:
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    while (low <= high):
        mid = (low + high) // 2
        if (nums[mid] <= target):
            low = mid + 1
        elif (nums[mid] > target):
            ans = mid
            high = mid - 1
    return ans


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first1 = first(nums, target)
        last1 = last(nums, target)
        if (first1 == -1):
            return [-1, -1]
        return [first1, last1]

    def searchRange_2(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first1 = lowerBound(nums, target)
        last1 = upperBound(nums, target) - 1
        if (first1 == n):
            return [-1, -1]
        elif (nums[first1] != target):
            return [-1, -1]
        return [first1, last1]

print(Solution().searchRange([5,7,7,8,8,10],8))
print(Solution().searchRange([5,7,7,8,8,10],6))
print(Solution().searchRange([],0))
print(Solution().searchRange_2([5,7,7,8,8,10],8))
print(Solution().searchRange_2([5,7,7,8,8,10],6))
print(Solution().searchRange_2([],0))

