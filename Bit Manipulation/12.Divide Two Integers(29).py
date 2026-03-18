class Solution:
    def divide_brute(self, dividend: int, divisor: int) -> int:
        sum = 0
        cnt = 0
        while (sum + divisor <= dividend):
            cnt += 1
            sum += divisor
        return cnt

    def divide(self, dividend: int, divisor: int) -> int:
        if (divisor == dividend):
            return 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = True
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = False
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while (n >= d):
            cnt = 0
            while (n >= (d << cnt+1)):
                cnt += 1
            n -= (d << cnt)
            ans += (1 << cnt)
        return ans if sign else (-1)*ans



print(Solution().divide_brute(22, 7))
print(Solution().divide(22, 7))