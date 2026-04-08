from typing import List

class Solution:
    def minWindow_brute(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        min_len = float('inf')
        s_index = -1
        for i in range(0, n):
            dict1 = {}
            cnt = 0
            for k in range(0, m):
                dict1[t[k]] = dict1.get(t[k], 0) + 1
            for j in range(i, n):
                if (s[j] in dict1 and dict1[s[j]] > 0):
                    dict1[s[j]] -= 1
                    cnt += 1
                if (cnt == m):
                    if (j-i+1 < min_len):
                        min_len = j-i+1
                        s_index = i
                    break
        return s[s_index:s_index+min_len] if s_index != -1 else ""

    def minWindow_optimal(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        min_len = float('inf')
        s_index = -1
        dict1 = {}
        cnt = 0
        l, r = 0, 0
        for i in range(0, m):
            dict1[t[i]] = dict1.get(t[i], 0) + 1
        while (r < n):
            if (s[r] in dict1):
                dict1[s[r]] -= 1
                if (dict1[s[r]] >= 0):
                    cnt += 1
            while (cnt == m and l <= r):
                if (r-l+1 < min_len):
                    min_len = r-l+1
                    s_index = l
                if (s[l] in dict1):
                    dict1[s[l]] += 1
                    if (dict1[s[l]] > 0):
                        cnt -= 1
                l += 1
            r += 1
        return s[s_index:s_index+min_len] if s_index != -1 else ""

print(Solution().minWindow_brute("ADOBECODEBANC", "ABC"))
print(Solution().minWindow_brute("a", "a"))
print(Solution().minWindow_brute("a", "aa"))
print(Solution().minWindow_optimal("ADOBECODEBANC", "ABC"))
print(Solution().minWindow_optimal("a", "a"))
print(Solution().minWindow_optimal("a", "aa"))