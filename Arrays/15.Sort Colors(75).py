from typing import List

class Solution:
    def sortColors_brute(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

    def sortColors_better(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt_0, cnt_1, cnt_2 = 0, 0, 0
        for i in range(0, n):
            if (nums[i] == 0):
                cnt_0 += 1
            elif (nums[i] == 1):
                cnt_1 += 1
            else:
                cnt_2 += 1
        for i in range(0, cnt_0):
            nums[i] = 0
        for i in range(cnt_0, cnt_0 + cnt_1):
            nums[i] = 1
        for i in range(cnt_0 + cnt_1, n):
            nums[i] = 2
        return nums

    def sortColors_optimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while (mid <= high):
            if (nums[mid] == 0):
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif (nums[mid] == 1):
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums




print(Solution().sortColors_brute([2,0,2,1,1,0]))
print(Solution().sortColors_brute([2,0,1]))
print(Solution().sortColors_better([2,0,2,1,1,0]))
print(Solution().sortColors_better([2,0,1]))
print(Solution().sortColors_optimal([2,0,2,1,1,0]))
print(Solution().sortColors_optimal([2,0,1]))