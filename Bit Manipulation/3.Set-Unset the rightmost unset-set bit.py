class Solution:
    def set_rightmost_unset_bit_brute(self, n):
        binary_str = bin(n)[2:]
        res = ""
        n =len(binary_str)
        flipped = False
        for i in range(n-1, -1, -1):
            if (binary_str[i] == '0' and not flipped):
                res = res + '1'
                flipped = True
            else:
                res = res + binary_str[i]
        if not flipped:
            res += '1'
        res = res[::-1]
        return int(res, 2)

    def set_rightmost_unset_bit(self, n):
        return n | (n + 1)

    def unset_rightmost_set_bit(self, n):
        return n & (n - 1)

print(Solution().set_rightmost_unset_bit_brute(10))
print(Solution().set_rightmost_unset_bit_brute(7))
print(Solution().set_rightmost_unset_bit(10))
print(Solution().set_rightmost_unset_bit(7))
print(Solution().unset_rightmost_set_bit(16))
print(Solution().unset_rightmost_set_bit(12))