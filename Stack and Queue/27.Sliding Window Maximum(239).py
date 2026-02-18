from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow_brute_1(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        start = 0
        end = k-1
        result = []
        while (end < n):
            maxi = nums[start]
            for i in range(start, end+1):
                maxi = max(maxi, nums[i])
            result.append(maxi)
            start += 1
            end += 1
        return result

    def maxSlidingWindow_brute_2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(0, n-k+1):
            maxi = nums[i]
            for j in range(i, i+k):
                maxi = max(maxi, nums[j])
            result.append(maxi)
        return result

    def maxSlidingWindow_optimal(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        dq = deque()
        for i in range(0, n):
            if (dq and dq[0] <= i-k):
                dq.popleft()
            while (dq and nums[dq[-1]] <= nums[i]):
                dq.pop()
            dq.append(i)
            if (i >= k-1):
                result.append(nums[dq[0]])
        return result

print(Solution().maxSlidingWindow_brute_1([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow_brute_1([1], 1))
print(Solution().maxSlidingWindow_brute_2([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow_brute_2([1], 1))
print(Solution().maxSlidingWindow_optimal([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow_optimal([1], 1))

