class Solution:
    def myPow_brute(self, x: float, n: int) -> float:
        ans = 1
        n1 = abs(n)
        for i in range(1, n1+1):
            ans = ans * x
        return ans if n > 0 else 1 / ans

    def myPow_optimal(self, x: float, n: int) -> float:
        ans = 1
        n1 = abs(n)
        while (n1 > 0):
            if (n1 % 2 == 0):
                x = x * x
                n1 = n1 / 2
            else:
                ans = ans * x
                n1 = n1 - 1
        return ans if n > 0 else 1 / ans

    def myPow_optimal_recursive(self, x: float, n: int) -> float:
        ans = 1
        if (n == 0):
            return 1
        if (n < 0):
            n = abs(n)
            x = 1/x
        if (n % 2 == 0):
            return self.myPow_optimal_recursive(x*x, n/2)
        else:
            return x * self.myPow_optimal_recursive(x, n-1)

print(Solution().myPow_brute(3, 3))
print(Solution().myPow_optimal(3,4))
print(Solution().myPow_optimal_recursive(2,5))
print(Solution().myPow_optimal_recursive(2,-5))
print(1/32)