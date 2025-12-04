from typing import List

class Solution:
    def majorityElement_brute(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            cnt = 0
            for j in range(0, n):
                if (nums[j] == nums[i]):
                    cnt += 1
            if (cnt > (n/2)):
                return nums[i]
        return -1

    def majorityElement_better(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {}
        for i in range(0, n):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1
        for key in dict1:
            if (dict1[key] > (n/2)):
                return key
        return -1

    def majorityElement_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        ele = None
        cnt = 0
        for i in range(0, n):
            if (cnt == 0):
                cnt = 1
                ele = nums[i]
            elif (nums[i] == ele):
                cnt += 1
            else:
                cnt -= 1
        cnt_1 = 0
        for i in range(0, n):
            if (nums[i] == ele):
                cnt_1 += 1
        if (cnt_1 > (n/2)):
            return ele
        return -1

print(Solution().majorityElement_brute([2,2,1,1,1,2,2]))
print(Solution().majorityElement_brute([3,2,3]))
print(Solution().majorityElement_better([2,2,1,1,1,2,2]))
print(Solution().majorityElement_better([3,2,3]))
print(Solution().majorityElement_optimal([2,2,1,1,1,2,2]))
print(Solution().majorityElement_optimal([3,2,3]))
print(Solution().majorityElement_optimal([2,2,1,1,1,2]))