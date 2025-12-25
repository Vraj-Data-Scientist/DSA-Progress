from typing import List

class Solution:
    def fourSum_brute(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        set1 = set()
        list1 = []
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if (nums[i] + nums[j] + nums[k] + nums[l] == target):
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            set1.add(tuple(temp))
        for key in set1:
            list1.append(list(key))
        return list1

    def fourSum_better(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        set1 = set()
        list1 = []
        for i in range(0, n):
            for j in range(i+1, n):
                set2 = set()
                for k in range(j+1, n):
                    if (target - (nums[i] + nums[j] + nums[k]) in set2):
                        temp = [nums[i], nums[j], nums[k], (target - (nums[i] + nums[j] + nums[k]))]
                        temp.sort()
                        set1.add(tuple(temp))
                    set2.add(nums[k])
        for key in set1:
            list1.append(list(key))
        return list1

    def fourSum_optimal(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        list1 = []
        nums.sort()
        for i in range(0, n):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1, n):
                if (j > i+1 and nums[j] == nums[j-1]):
                    continue
                k = j+1
                l = n-1
                while (k < l):
                    if ((nums[i] + nums[j] + nums[k] + nums[l]) == target):
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        list1.append(temp)
                        k += 1
                        l -= 1
                        while (k < l and nums[k] == nums[k-1]):
                            k += 1
                        while (k < l and nums[l] == nums[l+1]):
                            l -= 1
                    elif ((nums[i] + nums[j] + nums[k] + nums[l]) < target):
                        k += 1
                    else:
                        l -= 1
        return list1


print(Solution().fourSum_brute([1,0,-1,0,-2,2], 0))
print(Solution().fourSum_brute([2,2,2,2,2], 8))
print(Solution().fourSum_better([1,0,-1,0,-2,2], 0))
print(Solution().fourSum_better([2,2,2,2,2], 8))
print(Solution().fourSum_optimal([1,0,-1,0,-2,2], 0))
print(Solution().fourSum_optimal([2,2,2,2,2], 8))