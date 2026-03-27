class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(0, n):
            dict1 = {}
            for j in range(i, n):
                dict1[s[j]] = dict1.get(s[j], 0) + 1
                mini = min(dict1.values())
                maxi = max(dict1.values())
                total += (maxi - mini)
        return total

print(Solution().beautySum("aabcb"))
print(Solution().beautySum("aabcbaa"))

