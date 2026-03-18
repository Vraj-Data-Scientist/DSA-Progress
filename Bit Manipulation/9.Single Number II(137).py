from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {}
        for i in range(0, n):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1
        for key in dict1:
            if (dict1[key] == 1):
                return key
        return -1

    def singleNumber_better(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for bit_index in range(0, 32):
            cnt = 0
            for i in range(0, n):
                if (nums[i] & (1 << bit_index)):
                    cnt += 1
            if (cnt % 3 == 1):
                ans = ans | (1 << bit_index)
        if (ans & 1<<31):
            ans -= 1<<32
        return ans

    def singleNumber_better_2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1, n, 3):
            if (nums[i] != nums[i-1]):
                return nums[i-1]
        return nums[n-1]

    def singleNumber_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        ones = 0
        twos = 0
        for i in range(0, n):
            ones = (ones ^ nums[i]) & ~(twos)
            twos = (twos ^ nums[i]) & ~(ones)
        return ones

print(Solution().singleNumber([2,2,3,2]))
print(Solution().singleNumber([0,1,0,1,0,1,99]))
print(Solution().singleNumber_better([2,2,3,2]))
print(Solution().singleNumber_better([0,1,0,1,0,1,99]))
print(Solution().singleNumber_better_2([2,2,3,2]))
print(Solution().singleNumber_better_2([0,1,0,1,0,1,99]))
print(Solution().singleNumber_optimal([2,2,3,2]))
print(Solution().singleNumber_optimal([0,1,0,1,0,1,99]))