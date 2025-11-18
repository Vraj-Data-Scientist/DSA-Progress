from typing import List

class Solution:
    def moveZeroes_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = []
        for i in range(0,n):
            if (nums[i] != 0):
                temp.append(nums[i])
        for i in range(0, len(temp)):
            nums[i] = temp[i]
        for i in range(len(temp), n):
            nums[i] = 0
        return nums

    def moveZeroes_optimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0,n):
            if (nums[i] == 0):
                break
        for j in range(i+1, n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

print(Solution().moveZeroes_brute([0,1,0,3,12]))
print(Solution().moveZeroes_optimal([0,1,0,3,12]))