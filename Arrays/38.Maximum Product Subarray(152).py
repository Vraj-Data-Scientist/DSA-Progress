from typing import List

class Solution:
    def maxProduct_brute(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')
        for i in range(0, n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                maxi = max(maxi, product)
        return maxi

    def maxProduct_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        suff = 1
        pre = 1
        maxi = float('-inf')
        for i in range(0, n):
            if (pre == 0): pre = 1
            if (suff == 0): suff = 1
            pre *= nums[i]
            suff *= nums[n-i-1]
            maxi = max(maxi, max(pre, suff))
        return maxi




print(Solution().maxProduct_brute([2,3,-2,4]))
print(Solution().maxProduct_brute([-2,0,-1]))
print(Solution().maxProduct_optimal([2,3,-2,4]))
print(Solution().maxProduct_optimal([-2,0,-1]))
