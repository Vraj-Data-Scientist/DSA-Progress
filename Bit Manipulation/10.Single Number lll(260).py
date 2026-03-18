from typing import List

class Solution:
    def singleNumber_3(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {}
        ans = []
        for i in range(0, n):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1
        for key in dict1:
            if (dict1[key] == 1):
                ans.append(key)
        ans.sort()
        return ans

    def singleNumber_3_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(0, n):
            xor = xor ^ nums[i]
        rightmost = (xor & xor-1) ^ xor
        b1 = 0
        b2 = 0
        for i in range(0, n):
            if (nums[i] & rightmost):
                b1 = b1 ^ nums[i]
            else:
                b2 = b2 ^ nums[i]
        return [b1, b2] if b1<b2 else [b2, b1]

print(Solution().singleNumber_3( [1, 2, 1, 5, 3, 2]))
print(Solution().singleNumber_3_optimal( [1, 2, 1, 5, 3, 2]))
