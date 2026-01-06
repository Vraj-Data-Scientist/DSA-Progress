def pow1(x, n):
    m = n
    ans = 1
    while (n > 0):
        if (n % 2 == 1):
            ans = ans * x
            n = n - 1
        else:
            n //= 2
            x = x * x
    return ans if m > 0 else (1/ans)

print(pow1(3, 2))

class Solution:
    def mySqrt_brute(self, x: int) -> int:
        ans = 1
        for i in range(1, x+1):
            if (pow1(i, 2) <= x):
                ans = i
            else:
                break
        return ans

    def mySqrt_optimal(self, x: int) -> int:
        low = 1
        high = x
        ans = 1
        while (low <= high):
            mid = (low + high) // 2
            if (pow1(mid, 2) <= x):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


print(Solution().mySqrt_brute(36))
print(Solution().mySqrt_brute(28))
print(Solution().mySqrt_optimal(36))
print(Solution().mySqrt_optimal(28))






