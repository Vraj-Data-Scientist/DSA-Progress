class Solution:
    def minBitFlips_brute(self, start: int, goal: int) -> int:
        ans = start ^ goal
        cnt = 0
        for i in range(0, 32):
            if (ans & (1 << i)):
                cnt += 1
        return cnt

    def minBitFlips_better(self, start: int, goal: int) -> int:
        ans = start ^ goal
        cnt = 0
        while (ans > 0):
            cnt += (ans & 1)
            ans = ans >> 1
        return cnt

    def minBitFlips_optimal(self, start: int, goal: int) -> int:
        cnt = 0
        ans = start ^ goal
        while (ans != 0):
            ans = ans & (ans - 1)
            cnt += 1
        return cnt

print(Solution().minBitFlips_brute(10, 7))
print(Solution().minBitFlips_better(10, 7))
print(Solution().minBitFlips_optimal(10, 7))

