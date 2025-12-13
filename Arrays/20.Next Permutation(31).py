from typing import List

class Solution:

    def rev(self, a:List[int], start:int, end:int) -> None:
        while (start < end):
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1

    def nextPermutation_optimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index = -1
        for i in range(n-2, -1, -1):
            if (nums[i] < nums[i+1]):
                index = i
                break
        if (index == -1):
            nums.reverse()
            return nums
        for i in range(n-1, -1, -1):
            if (nums[index] < nums[i]):
                nums[index], nums[i] = nums[i], nums[index]
                break
        Solution().rev(nums, index+1, n-1)
        return nums

print(Solution().nextPermutation_optimal([3,2,1]))
print(Solution().nextPermutation_optimal([1,2,3]))
print(Solution().nextPermutation_optimal([1,1,5]))



