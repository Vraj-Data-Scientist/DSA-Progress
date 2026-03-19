from typing import List
import math
class Solution:
    def getDivisors_brute(self, N):
        ds = []
        for i in range(1, N+1):
            if (N % i == 0):
                ds.append(i)
        return ds

    def getDivisors_optimal(self, N):
        ds = []
        for i in range(1, int(math.sqrt(N))+1):
            if (N % i == 0):
                ds.append(i)
                if (N/i != i):
                    ds.append(int(N/i))
        ds.sort()
        return ds

    def checkPrime(self, n):
        cnt = 0
        for i in range(1, n+1):
            if (n % i == 0):
                cnt += 1
        return cnt == 2

    def checkPrime_optimal(self, n):
        cnt = 0
        for i in range(1, int(math.sqrt(n))+1):
            if (n % i == 0):
                cnt += 1
                if (n/i != i):
                    cnt += 1
        return cnt == 2

    def prime_factors_brute(self, n):
        list1 = []
        for i in range(2, n+1):
            if (n % i == 0):
                if (self.checkPrime(i)):
                    list1.append(i)
        return list1

    def prime_factors_better(self, n):
        list1 = []
        for i in range(2, int(math.sqrt(n))+1):
            if (n % i == 0):
                if (self.checkPrime_optimal(i)):
                    list1.append(i)
                if ((n/i) != i):
                    if (self.checkPrime_optimal(n/i)):
                        list1.append(int(n/i))
        return list1

    def prime_factors_optimal_1(self, n):
        list1 = []
        for i in range(2, n+1):
            if (n % i == 0):
                list1.append(i)
                while (n % i == 0):
                    n = n / i
        return list1

    def prime_factors_optimal_2(self, n):
        list1 = []
        for i in range(2, int(math.sqrt(n))+1):
            if (n % i == 0):
                list1.append(i)
                while (n % i == 0):
                    n = n / i
        if (n != 1):
            list1.append(n)
        return list1

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        set1 = set()
        n = len(nums)
        for i in range(0, n):
            for j in range(2, int(math.sqrt(nums[i]))+1):
                if (nums[i] % j == 0):
                    set1.add(j)
                    while (nums[i] % j == 0):
                        nums[i] = nums[i] / j
            if (nums[i] != 1):
                set1.add(nums[i])
        return len(set1)

print(Solution().distinctPrimeFactors([2,4,3,7,10,6]))
print(Solution().distinctPrimeFactors([2,4,8,16]))

