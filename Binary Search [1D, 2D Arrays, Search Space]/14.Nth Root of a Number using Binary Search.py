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
    def nthRoot_brute(self, n:int, m:int) -> int:
        for i in range(1, m+1):
            if (pow1(i, n) == m):
                return i
            elif (pow1(i, n) > m):
                break
        return -1

    def nthRoot_optimal(self, n:int, m:int) -> int:
        low = 1
        high = m
        while (low <= high):
            mid = (low + high) // 2
            if (pow1(n, mid) == m):
                return mid
            elif (pow1(n, mid) > m):
                high = mid - 1
            else:
                low = mid + 1
        return -1



print(Solution().nthRoot_brute(3, 27))
print(Solution().nthRoot_brute(4, 69))
print(Solution().nthRoot_optimal(3, 27))
print(Solution().nthRoot_optimal(4, 69))
