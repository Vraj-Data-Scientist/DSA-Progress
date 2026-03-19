import math
class Solution:
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

    # O(n * sqrt(n))
    def countPrimes_brute(self, n: int) -> int:
        cnt = 0
        for i in range(2, n):
            if (self.checkPrime_optimal(i)):
                cnt += 1
        return cnt

    def get_sieve_brute(self, n):
        prime = [1] * (n+1)
        prime[0] = 0
        if (n > 0):
            prime[1] = 0
        for i in range(2, n+1):
            if (prime[i] == 1):
                for j in range(2*i, n+1, i):
                    prime[j] = 0
        return prime

    def get_sieve(self, n):
        prime = [1] * (n+1)
        prime[0] = 0
        if (n > 0):
            prime[1] = 0
        for i in range(2, int(math.sqrt(n))+1):
            if (prime[i] == 1):
                for j in range(i*i, n+1, i):
                    prime[j] = 0
        return prime

    def countPrimes_optimal(self, n: int) -> int:
        cnt = 0
        prime = self.get_sieve(n)
        for i in range(2, n):
            if (prime[i]):
                cnt += 1
        return cnt


print(Solution().countPrimes_brute(10))
print(Solution().countPrimes_brute(0))
print(Solution().countPrimes_brute(1))
print(Solution().countPrimes_optimal(10))
print(Solution().countPrimes_optimal(0))
print(Solution().countPrimes_optimal(1))
print(Solution().countPrimes_optimal(999983))
