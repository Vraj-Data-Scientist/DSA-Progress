class Solution(object):
    def lengthOfLongestSubstring_brute(self, s):
        n = len(s)
        max_len = 0
        for i in range(0,n):
            dict1 = {i:0 for i in range(256)}
            for j in range(i,n):
                if (dict1[ord(s[j])] == 1):
                    break
                if (dict1[ord(s[j])] == 0):
                    dict1[ord(s[j])] = 1
                max_len = max(max_len, j-i+1)
        return max_len

    def lengthOfLongestSubstring_optimal(self, s):
        n = len(s)
        max_len = 0
        l = 0
        r = 0
        dict1 = {i:-1 for i in range(256)}
        while (r < n):
            if (dict1[ord(s[r])] != -1):
                if (dict1[ord(s[r])] >= l):
                    l = dict1[ord(s[r])] + 1
            dict1[ord(s[r])] = r
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len

print(Solution().lengthOfLongestSubstring_brute("pwwkew"))
print(Solution().lengthOfLongestSubstring_optimal("pwwkew"))