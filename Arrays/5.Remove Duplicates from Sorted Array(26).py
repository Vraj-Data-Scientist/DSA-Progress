from typing import List

class Solution:
    def removeDuplicates_brute(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {}
        for i in range(0,n):
            dict1[nums[i]] = i
        i = 0
        for item in dict1:
            nums[i] = item
            i += 1
        return i

    def removeDuplicates_optimal(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        for j in range(i+1, n):
            if (nums[j] != nums[i]):
                nums[i+1] = nums[j]
                i += 1
        return i + 1

print(Solution().removeDuplicates_brute([0,0,1,1,1,2,2,3,3,4]))
print(Solution().removeDuplicates_optimal([0,0,1,1,1,2,2,3,3,4]))
