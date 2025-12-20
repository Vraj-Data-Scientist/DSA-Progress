from typing import List

class Solution:
    def subarraySum_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0, n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if (curr_sum == k):
                    cnt += 1
        return cnt

    def subarraySum_optimal(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = 0
        cnt = 0
        dict1 = {}
        for i in range(0, n):
            pre_sum += nums[i]
            if (pre_sum == k):
                cnt += 1
            if ((pre_sum - k) in dict1):
                cnt += dict1[pre_sum - k]
            dict1[pre_sum] = dict1.get(pre_sum, 0) + 1
        return cnt


print(Solution().subarraySum_brute([1,1,1], 2))
print(Solution().subarraySum_brute([1,2,3], 3))
print(Solution().subarraySum_optimal([1,1,1], 2))
print(Solution().subarraySum_optimal([1,2,3], 3))

