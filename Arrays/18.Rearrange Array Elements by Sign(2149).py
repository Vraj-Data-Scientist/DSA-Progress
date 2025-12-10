from typing import List

class Solution:
    def rearrangeArray_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []
        for i in range(0, n):
            if (nums[i] >= 0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range(0, n//2):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        return nums

    def rearrangeArray_optimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = 0
        neg = 1
        ans = [None] * n
        for i in range(0, n):
            if (nums[i] >= 0):
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
        return ans

    def rearrangeArray_not_equal_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []
        for i in range(0, n):
            if (nums[i] >= 0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        n1 = len(pos)
        n2 = len(neg)
        if (n1 > n2):
            for i in range(0, n2):
                nums[2*i] = pos[i]
                nums[2*i+1] = neg[i]
            index = 2*n2
            for i in range(n2, n1):
                nums[index] = pos[i]
                index += 1
        else:
            for i in range(0, n1):
                nums[2*i] = pos[i]
                nums[2*i+1] = neg[i]
            index = 2*n1
            for i in range(n1, n2):
                nums[index] = neg[i]
                index += 1
        return nums

print(Solution().rearrangeArray_brute([3,1,-2,-5,2,-4]))
print(Solution().rearrangeArray_brute([-1,1]))
print(Solution().rearrangeArray_optimal([3,1,-2,-5,2,-4]))
print(Solution().rearrangeArray_optimal([-1,1]))
print(Solution().rearrangeArray_not_equal_brute([3,1,5,6,-2,-5,2,-4]))
print(Solution().rearrangeArray_not_equal_brute([-1,1,-2,-3,-9,3]))


