from typing import List

class Solution:
    def lengthOfLongestSubstringKDistinct_brute(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        for i in range(0, n):
            dict1 = {}
            for j in range(i, n):
                dict1[s[j]] = dict1.get(s[j], 0) + 1
                if (len(dict1) <= k):
                    max_len = max(max_len, j-i+1)
                if (len(dict1) > k):
                    break
        return max_len

    def lengthOfLongestSubstringKDistinct_optimal(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        l, r = 0, 0
        dict1 = {}
        while (r < n):
            dict1[s[r]] = dict1.get(s[r], 0) + 1
            while (len(dict1) > k):
                dict1[s[l]] -= 1
                if (dict1[s[l]] == 0):
                    del dict1[s[l]]
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len


print(Solution().lengthOfLongestSubstringKDistinct_brute("aababbcaacc", 2))
print(Solution().lengthOfLongestSubstringKDistinct_brute("abcddefg", 3))
print(Solution().lengthOfLongestSubstringKDistinct_optimal("aababbcaacc", 2))
print(Solution().lengthOfLongestSubstringKDistinct_optimal("abcddefg", 3))
