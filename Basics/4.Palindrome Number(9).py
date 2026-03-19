class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_int = 0
        x1 = x
        if (x1 < 0):
            return False
        while(x1 > 0):
            last_digit = x1 % 10
            rev_int = (rev_int * 10) + last_digit
            x1 = x1 // 10
        if (x > 0 and rev_int > 2**31-1):
            return False
        if (x < 0 and rev_int > 2**31):
            return False
        rev_int = rev_int if x>0 else -rev_int
        return rev_int == x

print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(111121111))
print(Solution().isPalindrome(11111111211111111))