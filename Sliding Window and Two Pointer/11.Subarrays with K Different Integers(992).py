from typing import List

class Solution:
    def subarraysWithKDistinct_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0, n):
            dict1 = {}
            for j in range(i, n):
                dict1[nums[j]] = dict1.get(nums[j], 0) + 1
                if (len(dict1) == k):
                    cnt += 1
                if (len(dict1) > k):
                    break
        return cnt

    def helper(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        dict1 = {}
        cnt = 0
        while (r < n):
            dict1[nums[r]] = dict1.get(nums[r], 0) + 1
            while (len(dict1) > k):
                dict1[nums[l]] -= 1
                if (dict1[nums[l]] == 0):
                    del dict1[nums[l]]
                l += 1
            cnt += (r-l+1)
            r += 1
        return cnt

    def subarraysWithKDistinct_optimal(self, nums: List[int], k: int) -> int:
        return (self.helper(nums, k) - self.helper(nums, k-1))


print(Solution().subarraysWithKDistinct_brute([1,2,1,2,3], 2))
print(Solution().subarraysWithKDistinct_brute([1,2,1,3,4], 3))
print(Solution().subarraysWithKDistinct_optimal([1,2,1,2,3], 2))
print(Solution().subarraysWithKDistinct_optimal([1,2,1,3,4], 3))
