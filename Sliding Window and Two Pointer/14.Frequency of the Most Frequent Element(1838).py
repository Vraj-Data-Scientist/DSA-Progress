from typing import List

class Solution:
    def maxFrequency_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 1
        for i in range(0, n):
            curr = 0
            for j in range(i, -1, -1):
                curr += nums[j]
                if (((i-j+1) * nums[i] - curr) > k):
                    break
                ans = max(ans, i-j+1)
        return ans

    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, 0
        curr = 0
        ans = 0
        while (r < n):
            curr += nums[r]
            while ((r-l+1) * nums[r] - curr > k):
                curr -= nums[l]
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans

print(Solution().maxFrequency_brute([1,2,4], 5))
print(Solution().maxFrequency_brute([1,4,8,13], 5))
print(Solution().maxFrequency([1,2,4], 5))
print(Solution().maxFrequency([1,4,8,13], 5))