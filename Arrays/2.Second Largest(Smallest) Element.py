class Solution:
    def secondLargestElement_brute(self, nums):
        n = len(nums)
        nums.sort()
        largest = nums[n-1]
        s_largest = float('-inf')
        for i in range(n-2, -1, -1):
            if (nums[i] != largest):
                s_largest = nums[i]
                break
        return s_largest

    def secondLargestElement_better(self, nums):
        n = len(nums)
        largest = nums[0]
        for i in range(1,n):
            if (nums[i] > largest):
                largest = nums[i]
        s_largest = float('-inf')
        for i in range(0,n):
            if (nums[i] != largest and nums[i] > s_largest):
                s_largest = nums[i]
        return s_largest

    def secondLargestElement_optimal(self, nums):
        n = len(nums)
        largest = nums[0]
        s_largest = float('-inf')
        for i in range(0,n):
            if (nums[i] > largest):
                s_largest = largest
                largest = nums[i]
            elif (nums[i] < largest and nums[i] > s_largest):
                s_largest = nums[i]
        return s_largest

print(Solution().secondLargestElement_brute([3, 7, 6, 7, 1, 7]))
print(Solution().secondLargestElement_better([3, 7, 6, 7, 1, 7]))
print(Solution().secondLargestElement_optimal([3, 7, 6, 7, 1, 7]))