from typing import List

class Solution:
    def threeSum_brute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        set1 = set()
        list1 = []
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if ((nums[i] + nums[j] + nums[k]) == 0):
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        set1.add(tuple(temp))
        for key in set1:
            list1.append(list(key))
        return list1

    def threeSum_better(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        list1 = []
        set1 = set()
        for i in range(0, n):
            set2 = set()
            for j in range(i+1, n):
                if (-(nums[i] + nums[j]) in set2):
                    temp = [nums[i], nums[j], -(nums[i] + nums[j])]
                    temp.sort()
                    set1.add(tuple(temp))
                set2.add(nums[j])
        for key in set1:
            list1.append(list(key))
        return list1

    def threeSum_optimal(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        list1 = []
        for i in range(0, n):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            j = i+1
            k = n-1
            while (j < k):
                if (nums[i] + nums[j] + nums[k] < 0):
                    j += 1
                    while (nums[j] == nums[j-1] and j < k):
                        j += 1
                elif (nums[i] + nums[j] + nums[k] > 0):
                    k -= 1
                    while (nums[k] == nums[k+1] and j < k):
                        k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    list1.append(temp)
                    j += 1
                    k -= 1
                    while (nums[j] == nums[j-1] and j < k):
                        j += 1
                    while (nums[k] == nums[k+1] and j < k):
                        k -= 1
        return list1

print(Solution().threeSum_brute([-1,0,1,2,-1,-4]))
print(Solution().threeSum_brute([0,1,1]))
print(Solution().threeSum_brute([0,0,0]))
print(Solution().threeSum_better([-1,0,1,2,-1,-4]))
print(Solution().threeSum_better([0,1,1]))
print(Solution().threeSum_better([0,0,0]))
print(Solution().threeSum_optimal([-1,0,1,2,-1,-4]))
print(Solution().threeSum_optimal([0,1,1]))
print(Solution().threeSum_optimal([0,0,0]))
