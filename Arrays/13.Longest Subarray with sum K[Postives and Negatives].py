from typing import List

class Solution:
    def longest_subarray_sum_k_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0
        for i in range(0, n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if (curr_sum == k):
                    max_len = max(max_len, j-i+1)
        return max_len if max_len else 0

    def longest_subarray_sum_k_optimal(self, nums: List[int], k:int) -> int:
        n = len(nums)
        max_len = 0
        pre_sum = 0
        dict1 = {}
        i = 0
        for j in range(0, n):
            pre_sum += nums[j]
            temp = pre_sum - k
            if (pre_sum == k):
                max_len = max(max_len, j+1)
            elif (temp in dict1):
                max_len = max(max_len, j - dict1[temp])
            if pre_sum not in dict1:
                dict1[pre_sum] = j
        return max_len if max_len else 0


print(Solution().longest_subarray_sum_k_brute([-1, 1, 1, -1, 1, 3, -2], 1))
print(Solution().longest_subarray_sum_k_brute([10, 5, 2, 7, 1, 9], 15))
print(Solution().longest_subarray_sum_k_brute([-3, 2, 1], 6))
print(Solution().longest_subarray_sum_k_optimal([-1, 1, 1, -1, 1, 3, -2], 1))
print(Solution().longest_subarray_sum_k_optimal([10, 5, 2, 7, 1, 9], 15))
print(Solution().longest_subarray_sum_k_optimal([-3, 2, 1], 6))
