from typing import List

class Solution:
    def cnt_subarray_xor_k_brute(self, nums:List[int], k:int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0, n):
            xor = 0
            for j in range(i, n):
                xor = xor ^ nums[j]
                if (xor == k):
                    cnt += 1
        return cnt

    def cnt_subarray_xor_k_optimal(self, nums:List[int], k:int) -> int:
        n = len(nums)
        dict1 = {}
        cnt = 0
        pre_xor = 0
        for i in range(0, n):
            pre_xor = pre_xor ^ nums[i]
            if (pre_xor == k):
                cnt += 1
            if ((pre_xor ^ k) in dict1):
                cnt += dict1[pre_xor ^ k]
            dict1[pre_xor] = dict1.get(pre_xor, 0) + 1
        return cnt



print(Solution().cnt_subarray_xor_k_brute([4, 2, 2, 6, 4], 6))
print(Solution().cnt_subarray_xor_k_brute([5, 6, 7, 8, 9], 5))
print(Solution().cnt_subarray_xor_k_optimal([4, 2, 2, 6, 4], 6))
print(Solution().cnt_subarray_xor_k_optimal([5, 6, 7, 8, 9], 5))
