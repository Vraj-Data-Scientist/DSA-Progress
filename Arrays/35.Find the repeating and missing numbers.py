from typing import List

class Solution:
    def repeating_and_missing_brute(self, nums:List[int]) -> List[int]:
        n = len(nums)
        repeating = -1
        missing = -1
        for i in range(1, n+1):
            cnt = 0
            for j in range(0, n):
                if (nums[j] == i):
                    cnt += 1
            if (cnt == 2):
                repeating = i
            elif (cnt == 0):
                missing = i
            if ((repeating != -1) and (missing != -1)):
                break
        return [repeating, missing]

    def repeating_and_missing_better(self, nums:List[int]) -> List[int]:
        n = len(nums)
        hash = [0]*(n+1)
        for i in range(0, n):
            hash[nums[i]] += 1
        repeating = -1
        missing = -1
        for i in range(1, n+1):
            if (hash[i] == 2):
                repeating = i
            elif (hash[i] == 0):
                missing = i
            if ((repeating != -1) and (missing != -1)):
                break
        return [repeating, missing]

    def repeating_and_missing_optimal_1(self, nums:List[int]) -> List[int]:
        n = len(nums)
        sn = (n*(n+1))/2
        sn2 = (n*(n+1)*(2*n+1))/6
        s = 0
        s2 = 0
        for i in range(0, n):
            s += nums[i]
            s2 += (nums[i] * nums[i])
        value1 = s - sn
        value2 = s2 - sn2
        # ----- after solving we get two variables
        sum_rm = value2 // value1
        x = (sum_rm + value1) // 2
        y = (sum_rm - value1) // 2
        cnt = 0
        for i in range(0, n):
            if (nums[i] == x):
                cnt += 1
        if (cnt == 2): return [int(x), int(y)]
        return [int(y), int(x)]

    def repeating_and_missing_optimal_2(self, nums:List[int]) -> List[int]:
        n = len(nums)
        xr = 0
        for i in range(0, n):
            xr = xr ^ nums[i]
            xr = xr ^ (i+1)
        diff_bit = 0
        while(1):
            if ((xr & (1<<diff_bit)) != 0):
                break
            diff_bit += 1
        ones = 0
        zeros = 0
        for i in range(0, n):
            if ((nums[i] & (1<<diff_bit)) != 0):
                ones = ones ^ nums[i]
            else:
                zeros = zeros ^ nums[i]
        for i in range(1, n+1):
            if ((i & (1<<diff_bit)) != 0):
                ones = ones ^ i
            else:
                zeros = zeros ^ i
        cnt = 0
        for i in range(0, n):
            if (nums[i] == zeros):
                cnt += 1
        if (cnt == 2): return [zeros, ones]
        return [ones, zeros]





print(Solution().repeating_and_missing_brute([3, 5, 4, 1, 1]))
print(Solution().repeating_and_missing_brute([1, 2, 3, 6, 7, 5, 7]))
print(Solution().repeating_and_missing_better([3, 5, 4, 1, 1]))
print(Solution().repeating_and_missing_better([1, 2, 3, 6, 7, 5, 7]))
print(Solution().repeating_and_missing_optimal_1([3, 5, 4, 1, 1]))
print(Solution().repeating_and_missing_optimal_1([1, 2, 3, 6, 7, 5, 7]))
print(Solution().repeating_and_missing_optimal_2([3, 5, 4, 1, 1]))
print(Solution().repeating_and_missing_optimal_2([1, 2, 3, 6, 7, 5, 7]))