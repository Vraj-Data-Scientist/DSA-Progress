from typing import List

class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []

    def twoSum_better(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        for i in range(0, n):
            if ((target - nums[i]) in dict1):
                return [dict1[target - nums[i]], i]
            dict1[nums[i]] = i
        return []

    def twoSum_optimal(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        left = 0
        right = n-1
        while (left < right):
            if (nums[left] + nums[right] < target):
                left += 1
            elif (nums[left] + nums[right] > target):
                right -= 1
            else:
                return True
        return False






print(Solution().twoSum_brute([2,7,11,15], 9))
print(Solution().twoSum_brute([3,2,4], 6))
print(Solution().twoSum_brute([3,3], 6))
print(Solution().twoSum_better([2,7,11,15], 9))
print(Solution().twoSum_better([3,2,4], 6))
print(Solution().twoSum_better([3,3], 6))
print(Solution().twoSum_optimal([2,7,11,15], 9))
print(Solution().twoSum_optimal([3,2,4], 6))
print(Solution().twoSum_optimal([3,3], 6))
print(Solution().twoSum_optimal([2,7,11,15], 10))
