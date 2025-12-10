from typing import List

class Solution:
    def maxSubArray_brute(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(0, n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        return max_sum

    def maxSubArray_optimal(self, nums: List[int]) -> (int, int, int, List[int]):
        n = len(nums)
        max_sum = float('-inf')
        curr_sum = 0
        start = None
        ans_start = None
        ans_end = None
        for i in range(0, n):
            if (curr_sum == 0):
                start = i
            curr_sum += nums[i]
            if (curr_sum > max_sum):
                max_sum = curr_sum
                ans_start = start
                ans_end = i
            if (curr_sum < 0):
                curr_sum = 0
        return ans_start, ans_end, max_sum, nums[ans_start:ans_end+1]

print(Solution().maxSubArray_brute([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray_brute([5,4,-1,7,8]))
print(Solution().maxSubArray_brute([1]))
print(Solution().maxSubArray_optimal([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray_optimal([5,4,-1,7,8]))
print(Solution().maxSubArray_optimal([1]))
print(Solution().maxSubArray_optimal([-1]))
