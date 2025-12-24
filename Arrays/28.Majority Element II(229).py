from typing import List

class Solution:
    def majorityElement_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        list1 = []
        for i in range(0, n):
            cnt = 0
            if (len(list1) == 0 or list1[0] != nums[i]):
                for j in range(0, n):
                    if (nums[j] == nums[i]):
                        cnt += 1
                if (cnt > (n//3)):
                    list1.append(nums[i])
            if (len(list1) == 2):
                break
        return list1

    def majorityElement_better(self, nums: List[int]) -> List[int]:
        list1 = []
        dict1 = {}
        n = len(nums)
        for i in range(0, n):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1
            if (len(list1) == 0 or list1[0] != nums[i]):
                if (dict1[nums[i]] > (n//3)):
                    list1.append(nums[i])
            if (len(list1) == 2):
                break
        return list1

    def majorityElement_optimal(self, nums: List[int]) -> List[int]:
        list1 = []
        n = len(nums)
        ele1 = None
        cnt1 = 0
        ele2 = None
        cnt2 = 0
        for i in range(0, n):
            if (cnt1 == 0 and nums[i] != ele2):
                ele1 = nums[i]
                cnt1 += 1
            elif (cnt2 == 0 and nums[i] != ele1):
                ele2 = nums[i]
                cnt2 += 1
            elif (nums[i] == ele1):
                cnt1 += 1
            elif (nums[i] == ele2):
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt11 = 0
        cnt22 = 0
        for i in range(0, n):
            if (ele1 == nums[i]):
                cnt11 += 1
            if (ele2 == nums[i]):
                cnt22 += 1
        if (cnt11 > (n//3)):
            list1.append(ele1)
        if (cnt22 > (n//3)):
            list1.append(ele2)
        return list1






print(Solution().majorityElement_brute([3,2,3]))
print(Solution().majorityElement_brute([1]))
print(Solution().majorityElement_brute([1,2]))
print(Solution().majorityElement_better([3,2,3]))
print(Solution().majorityElement_better([1]))
print(Solution().majorityElement_better([1,2]))
print(Solution().majorityElement_optimal([3,2,3]))
print(Solution().majorityElement_optimal([1]))
print(Solution().majorityElement_optimal([1,2]))

