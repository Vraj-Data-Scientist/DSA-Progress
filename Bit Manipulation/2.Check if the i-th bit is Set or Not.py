class Solution:
    def check_ith_bit_brute(self, n, i):
        binary = bin(n)[2:]
        if i >= len(binary):
            return False
        return binary[-(i+1)] == "1"

    def check_ith_bit_1(self, n, i):
        return (n & (1 << i)) != 0

    def check_ith_bit_2(self, n, i):
        return ((n >> i) & 1) != 0

    def set_ith_bit(self, n, i):
        return n | (1 << i)

    def clear_ith_bit(self, n, i):
        return n & ~(1 << i)

    def toggle_ith_bit(self, n, i):
        return n ^ (1 << i)

print(Solution().check_ith_bit_brute(5, 2))
print(Solution().check_ith_bit_1(5, 2))
print(Solution().check_ith_bit_2(5, 1))
print(Solution().set_ith_bit(9, 2))
print(Solution().clear_ith_bit(13,2))
print(Solution().toggle_ith_bit(13, 2))
