from typing import List

def count_split_given_max_sum(nums:List[int], max_sum:int):
    n = len(nums)
    split = 1
    sum = 0
    for i in range(0, n):
        if (sum + nums[i] <= max_sum):
            sum += nums[i]
        else:
            split += 1
            sum = nums[i]
    return split

class Solution:
    def splitArray_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if (k > n):
            return -1
        low = max(nums)
        high = sum(nums)
        for i in range(low, high+1):
            if (count_split_given_max_sum(nums, i) == k):
                return i
        return low

    def splitArray_optimal(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if (k > n):
            return -1
        low = max(nums)
        high = sum(nums)
        while (low <= high):
            mid = (low + high) // 2
            if (count_split_given_max_sum(nums, mid) > k):
                low = mid + 1
            else:
                high = mid - 1
        return low


print(Solution().splitArray_brute([7,2,5,10,8], 2))
print(Solution().splitArray_brute([1,2,3,4,5], 2))
print(Solution().splitArray_optimal([7,2,5,10,8], 2))
print(Solution().splitArray_optimal([1,2,3,4,5], 2))
