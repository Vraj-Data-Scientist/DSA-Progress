class Solution(object):
    def characterReplacement_brute(self, s, k):
        n = len(s)
        max_len = 0
        for i in range(0,n):
            dict1 = {i:0 for i in range(26)}
            max_freq = 0
            for j in range(i,n):
                dict1[ord(s[j]) - ord('A')] += 1
                max_freq = max(max_freq, dict1[ord(s[j]) - ord('A')])
                if (((j-i+1) - max_freq) > k):
                    break
                if (((j-i+1) - max_freq) <= k):
                    max_len = max(max_len, j-i+1)
        return max_len

    def characterReplacement_better(self, s, k):
        n = len(s)
        max_len = 0
        l = 0
        r = 0
        dict1 = {i:0 for i in range(26)}
        max_freq = 0
        while (r < n):
            dict1[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, dict1[ord(s[r]) - ord('A')])
            while (((r-l+1) - max_freq) > k):
                dict1[ord(s[l]) - ord('A')] -= 1
                max_freq = 0
                for i in range(0,26):
                    max_freq = max(max_freq, dict1[i])
                l += 1
            if (((r-l+1) - max_freq) <= k):
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len

    def characterReplacement_optimal(self, s, k):
        n = len(s)
        max_len = 0
        l = 0
        r = 0
        dict1 = {i:0 for i in range(26)}
        max_freq = 0
        while (r < n):
            dict1[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, dict1[ord(s[r]) - ord('A')])
            if (((r-l+1) - max_freq) > k):
                dict1[ord(s[l]) - ord('A')] -= 1
                max_freq = 0
                for i in range(0,26):
                    max_freq = max(max_freq, dict1[i])
                l += 1
            if (((r-l+1) - max_freq) <= k):
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len

print(Solution().characterReplacement_brute("ABAB",2))
print(Solution().characterReplacement_optimal("ABABCDBBBBBBB",2))
