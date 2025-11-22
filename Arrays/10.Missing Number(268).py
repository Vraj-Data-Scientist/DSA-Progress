from typing import List

class Solution:
    def missingNumber_brute(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n+1):
            item = i
            flag = 0
            for j in range(0, n):
                if (nums[j] == item):
                    flag = 1
                    break
            if (flag == 0):
                return item
        return -1

    def missingNumber_better(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {i:0 for i in range(0,n+1)}
        for i in range(0,n):
            dict1[nums[i]] = 1
        for i in range(0, n+1):
            if (dict1[i] == 0):
                return i
        return -1

    def missingNumber_optimal2(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = 0
        xor2 = 0
        for i in range(0, n+1):
            xor1 ^= i
        for i in range(0, n):
            xor2 ^= nums[i]
        return xor1 ^ xor2

    def missingNumber_optimal1(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = int(n*(n+1)/2)
        sum2 = 0
        for i in range(0, n):
            sum2 += nums[i]
        return (sum1-sum2)

print(Solution().missingNumber_brute([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber_better([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber_optimal2([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber_optimal1([9,6,4,2,3,5,7,0,1]))