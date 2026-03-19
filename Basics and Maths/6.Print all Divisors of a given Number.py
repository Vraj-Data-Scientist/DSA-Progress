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


print(Solution().getDivisors_brute(36))
print(Solution().getDivisors_brute(11))
print(Solution().getDivisors_brute(121))
print(Solution().getDivisors_optimal(36))
print(Solution().getDivisors_optimal(11))
print(Solution().getDivisors_optimal(121))