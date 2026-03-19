class Solution:
    def reverse(self, x: int) -> int:
        rev_int = 0
        x1 = abs(x)
        while(x1 > 0):
            last_digit = x1 % 10
            rev_int = (rev_int * 10) + last_digit
            x1 = x1 // 10
        if (x > 0 and rev_int > 2**31-1):
            return 0
        if (x < 0 and rev_int > 2**31):
            return 0
        return rev_int if x>0 else -rev_int

print(Solution().reverse(-12345678989898989898))
print(Solution().reverse(23456))