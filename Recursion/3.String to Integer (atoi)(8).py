class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        i = 0
        while (i < n and s[i] == ' '):
            i += 1
        if (i == n):
            return 0
        sign = 1
        if (s[i] == '+'):
            i += 1
        elif (s[i] == '-'):
            sign = -1
            i += 1
        res = 0
        int_min = -2**31
        int_max = 2**31 - 1
        while (i < n and s[i].isdigit()):
            digit = int(s[i])
            res = res * 10 + digit
            if (res * sign) <= int_min:
                return int_min
            if (res * sign) >= int_max:
                return int_max
            i += 1
        return res*sign

    def myAtoi_recursive(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        i = 0
        while (i < n and s[i] == ' '):
            i += 1
        if (i == n):
            return 0
        sign = 1
        if (s[i] == '+'):
            i += 1
        elif (s[i] == '-'):
            sign = -1
            i += 1
        return self.helper(s, i, sign, 0)

    def helper(self, s, i, sign, res):
        n = len(s)
        int_min = -2**31
        int_max = 2**31 - 1
        if (i >= n or not s[i].isdigit()):
            return res*sign
        digit = int(s[i])
        res = res * 10 + digit
        if (res * sign) <= int_min:
            return int_min
        if (res * sign) >= int_max:
            return int_max
        return self.helper(s, i+1, sign, res)

print(Solution().myAtoi("42"))
print(Solution().myAtoi("   -042"))
print(Solution().myAtoi("1337c0d3"))
print(Solution().myAtoi_recursive("42"))
print(Solution().myAtoi_recursive("   -042"))
print(Solution().myAtoi_recursive("1337c0d3"))