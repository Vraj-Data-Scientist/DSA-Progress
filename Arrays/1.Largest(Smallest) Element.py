class Solution:
    def largestElement_brute(self, nums):
        n = len(nums)
        nums.sort()
        largest = nums[n-1]
        return largest

    def largestElement_optimal(self, nums):
        n = len(nums)
        largest = nums[0]
        for i in range(1,n):
            if (nums[i] > largest):
                largest = nums[i]
        return largest

print(Solution().largestElement_brute([3, 3, 6, 7, 1]))
print(Solution().largestElement_optimal([3, 3, 6, 7, 1]))
