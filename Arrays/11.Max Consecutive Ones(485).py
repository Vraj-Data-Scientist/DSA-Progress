from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        max_len = 0
        for i in range(0, n):
            if (nums[i] == 1):
                cnt += 1
                max_len = max(max_len, cnt)
            else:
                cnt = 0
        return max_len

print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1,1,1]))