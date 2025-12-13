from typing import List

class Solution:
    def leaders_brute(self, nums:List[int]) -> List[int]:
        n = len(nums)
        list1 = []
        for i in range(0, n):
            leaders = True
            for j in range(i+1, n):
                if (nums[i] < nums[j]):
                    leaders = False
                    break
            if (leaders == True):
                list1.append(nums[i])
        return list1

    def leaders_optimal(self, nums:List[int]) -> List[int]:
        n = len(nums)
        list1 = []
        maxi = nums[n-1]
        for i in range(n-1, -1, -1):
            if (nums[i] >= maxi):
                list1.append(nums[i])
            maxi = max(maxi, nums[i])
        list1.reverse()
        return list1




print(Solution().leaders_brute([1, 2, 5, 3, 1, 2]))
print(Solution().leaders_brute([-3, 4, 5, 1, -4, -5]))
print(Solution().leaders_optimal([1, 2, 5, 3, 1, 2]))
print(Solution().leaders_optimal([-3, 4, 5, 1, -4, -5]))