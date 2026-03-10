class Solution:
    def check_ith_bit_brute(self, n, i):
        binary = bin(n)[2:]
        if i >= len(binary):
            return False
        return binary[-(i+1)] == "1"

    def check_ith_bit_optimal_1(self, n, i):
        return (n & (1 << i)) != 0

    def check_ith_bit_optimal_2(self, n, i):
        return ((n >> i) & 1) != 0

print(Solution().check_ith_bit_brute(5, 2))
print(Solution().check_ith_bit_brute(5, 1))
print(Solution().check_ith_bit_brute(5, 25))
print(Solution().check_ith_bit_optimal_1(5, 2))
print(Solution().check_ith_bit_optimal_1(5, 1))
print(Solution().check_ith_bit_optimal_1(5, 25))
print(Solution().check_ith_bit_optimal_2(5, 2))
print(Solution().check_ith_bit_optimal_2(5, 1))
print(Solution().check_ith_bit_optimal_2(5, 25))