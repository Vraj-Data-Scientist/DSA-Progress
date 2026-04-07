from typing import List

class Solution:
    def numberOfSubarrays_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dict1 = {}
        cnt = 0
        for i in range(0, n):
            cnt_odd = 0
            for j in range(i, n):
                if (nums[j] % 2 == 1):
                    cnt_odd += 1
                if (cnt_odd > k):
                    break
                if (cnt_odd == k):
                    cnt += 1
        return cnt

    def numberOfSubarrays_better(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dict1 = {}
        cnt = 0
        odd_cnt = 0
        for i in range(0, n):
            if (nums[i] % 2 == 1):
                odd_cnt += 1
            if (odd_cnt == k):
                cnt += 1
            if (odd_cnt - k in dict1):
                cnt += dict1[odd_cnt - k]
            dict1[odd_cnt] = dict1.get(odd_cnt, 0) + 1
        return cnt

    def helper(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        l, r = 0, 0
        cnt_odd = 0
        while (r < n):
            if (nums[r] % 2 == 1):
                cnt_odd += 1
            while (cnt_odd > k):
                if (nums[l] % 2 == 1):
                    cnt_odd -= 1
                l += 1
            cnt += (r-l+1)
            r += 1
        return cnt

    def numberOfSubarrays_optimal(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k-1)

print(Solution().numberOfSubarrays_brute([1,1,2,1,1], 3))
print(Solution().numberOfSubarrays_brute([2,4,6], 1))
print(Solution().numberOfSubarrays_brute([2,2,2,1,2,2,1,2,2,2], 2))
print(Solution().numberOfSubarrays_better([1,1,2,1,1], 3))
print(Solution().numberOfSubarrays_better([2,4,6], 1))
print(Solution().numberOfSubarrays_better([2,2,2,1,2,2,1,2,2,2], 2))
print(Solution().numberOfSubarrays_optimal([1,1,2,1,1], 3))
print(Solution().numberOfSubarrays_optimal([2,4,6], 1))
print(Solution().numberOfSubarrays_optimal([2,2,2,1,2,2,1,2,2,2], 2))