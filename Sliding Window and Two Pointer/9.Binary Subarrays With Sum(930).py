from typing import List

class Solution:
    def numSubarraysWithSum_brute(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0, n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if (sum == goal):
                    cnt += 1
        return cnt

    def numSubarraysWithSum_better(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        cnt = 0
        pre_sum = 0
        dict1 = {}
        for i in range(0, n):
            pre_sum += nums[i]
            if (pre_sum == goal):
                cnt += 1
            if (pre_sum - goal in dict1):
                cnt += dict1[pre_sum - goal]
            dict1[pre_sum] = dict1.get(pre_sum, 0) + 1
        return cnt

    def helper(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        if goal < 0:
            return 0
        l, r = 0, 0
        sum = 0
        cnt = 0
        while (r < n):
            sum += nums[r]
            while (sum > goal):
                sum -= nums[l]
                l += 1
            cnt += (r-l+1)
            r += 1
        return cnt

    def numSubarraysWithSum_optimal(self, nums: List[int], goal: int) -> int:
        return (self.helper(nums, goal) - self.helper(nums, goal-1))


print(Solution().numSubarraysWithSum_brute([1,0,1,0,1], 2))
print(Solution().numSubarraysWithSum_better([1,0,1,0,1], 2))
print(Solution().numSubarraysWithSum_optimal([1,0,1,0,1], 2))
