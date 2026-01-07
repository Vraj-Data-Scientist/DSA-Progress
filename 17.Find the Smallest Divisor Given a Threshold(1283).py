from typing import List
from math import ceil

def sum1(nums:List[int], divisor:int) -> int:
    n = len(nums)
    ans = 0
    for i in range(0, n):
        ans += ceil(nums[i] / divisor)
    return ans

print(sum1([1,2,5,9],4))
print(sum1([1,2,5,9],5))

class Solution:
    def smallestDivisor_brute(self, nums: List[int], threshold: int) -> int:
        for i in range(1, max(nums)+1):
            if (sum1(nums,i) <= threshold):
                return i
        return -1

    def smallestDivisor_optimal(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if (n > threshold):
            return -1
        low = 1
        high = max(nums)
        while (low <= high):
            mid = (low + high) // 2
            if (sum1(nums, mid) <= threshold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution().smallestDivisor_brute([1,2,5,9], 6))
print(Solution().smallestDivisor_brute([44,22,33,11,1], 5))
print(Solution().smallestDivisor_optimal([1,2,5,9], 6))
print(Solution().smallestDivisor_optimal([44,22,33,11,1], 5))
