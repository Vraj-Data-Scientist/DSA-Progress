class Solution:
    def pow(self, x, n):
        mod = 10**9 + 7
        n1 = abs(n)
        ans = 1
        while (n1 > 0):
            if (n1 % 2 == 1):
                ans = (ans * x) % mod
                n1 = n1 - 1
            else:
                x = (x * x) % mod
                n1 = n1 / 2
        return ans if n > 0 else 1/ans

    def myPow(self, x: float, n: int) -> float:
        mod = 10**9 + 7
        ans = 1
        if (n == 0):
            return 1
        if (n < 0):
            n = abs(n)
            x = 1/x
        if (n % 2 == 0):
            return self.myPow( (x*x)%mod , n/2)
        else:
            return (x * self.myPow(x, n-1)) % mod

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        return int(self.pow(5, (n+1)//2) * self.pow(4, n//2) % mod)

    def countGoodNumbers_recursive(self, n: int) -> int:
        mod = 10**9 + 7
        return int(self.myPow(5, (n+1)//2) * self.myPow(4, n//2) % mod)

print(Solution().countGoodNumbers(1))
print(Solution().countGoodNumbers(4))
print(Solution().countGoodNumbers_recursive(1))
print(Solution().countGoodNumbers_recursive(4))
