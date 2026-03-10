class Solution:
    def is_odd(self, n):
        return n % 2 == 1

    def is_odd_faster(self, n):
        return (n & 1 == 1)

print(Solution().is_odd(13))
print(Solution().is_odd(132))
print(Solution().is_odd_faster(13))
print(Solution().is_odd_faster(132))
