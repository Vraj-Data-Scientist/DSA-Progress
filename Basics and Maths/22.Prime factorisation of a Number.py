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

    def get_sieve(self, n):
        spf = [i for i in range(0, n+1)]
        for i in range(2, int(math.sqrt(n))+1):
            if (spf[i] == i):
                for j in range(i*i, n+1, i):
                    if (spf[j] == j):
                        spf[j] = i
        return spf

    def prime_factorization_for_diff_queries(self, q):
        result = []
        n = len(q)
        spf = self.get_sieve(max(q))
        for i in range(0, n):
            list1 = []
            n1 = q[i]
            while (n1 != 1):
                list1.append(spf[n1])
                n1 = int(n1 / spf[n1])
            result.append(list1)
        return result

print(Solution().prime_factors_brute(60))
print(Solution().prime_factors_brute(35))
print(Solution().prime_factors_brute(780))
print(Solution().prime_factors_better(60))
print(Solution().prime_factors_better(35))
print(Solution().prime_factors_better(780))
print(Solution().prime_factors_optimal_1(60))
print(Solution().prime_factors_optimal_1(35))
print(Solution().prime_factors_optimal_1(780))
print(Solution().prime_factors_optimal_2(60))
print(Solution().prime_factors_optimal_2(35))
print(Solution().prime_factors_optimal_2(780))
print(Solution().prime_factorization_for_diff_queries([12,16,60]))