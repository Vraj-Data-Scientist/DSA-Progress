from typing import List

class Solution:
    def singleNumber_brute(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            item = nums[i]
            cnt = 0
            for j in range(0, n):
                if (nums[j] == item):
                    cnt += 1
            if (cnt == 1):
                return item
        return -1

    def singleNumber_better(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {}
        for i in range(0, n):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1
        for i in range(0, n):
            if (dict1[nums[i]] == 1):
                return nums[i]
        return -1

    def singleNumber_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(0,n):
            xor ^= nums[i]
        return xor

print(Solution().singleNumber_brute([4,1,2,1,2]))
print(Solution().singleNumber_better([4,1,2,1,2]))
print(Solution().singleNumber_optimal([4,1,2,1,2]))