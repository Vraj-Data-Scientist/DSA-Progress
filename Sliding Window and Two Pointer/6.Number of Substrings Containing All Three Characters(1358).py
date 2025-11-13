class Solution(object):
    def numberOfSubstrings_brute(self, s):
        n = len(s)
        cnt = 0
        for i in range(0,n):
            dict1 = {i:0 for i in range(3)}
            for j in range(i, n):
                dict1[ord(s[j]) - ord('a')] = 1
                if (dict1[0] + dict1[1] + dict1[2] == 3):
                    cnt += (n-j)
                    break
        return cnt

    def numberOfSubstrings_optimal(self, s):
        n = len(s)
        cnt = 0
        dict1 = {i:-1 for i in range(3)}
        for i in range(0,n):
            dict1[ord(s[i]) - ord('a')] = i
            if (dict1[0] != -1 and dict1[1] != -1 and dict1[2] != -1):
                cnt += (1 + min(dict1[0], dict1[1], dict1[2]))
        return cnt

print(Solution().numberOfSubstrings_brute('abcabc'))
print(Solution().numberOfSubstrings_optimal('abcabc'))