class Solution:
    def cnt_set_bit_slower(self, n):
        cnt = 0
        while (n > 0):
            if (n % 2 == 1):
                cnt += 1
            n = n // 2
        return cnt

    def cnt_set_bit_faster(self, n):
        cnt = 0
        while (n > 0):
            cnt += (n & 1)
            n = n >> 1
        return cnt

    def cnt_set_bit_optimal(self, n):
        cnt = 0
        while (n != 0):
            n = n & (n-1)
            cnt += 1
        return cnt

print(Solution().cnt_set_bit_slower(5))
print(Solution().cnt_set_bit_slower(15))
print(Solution().cnt_set_bit_faster(5))
print(Solution().cnt_set_bit_faster(15))
print(Solution().cnt_set_bit_optimal(5))
print(Solution().cnt_set_bit_optimal(15))