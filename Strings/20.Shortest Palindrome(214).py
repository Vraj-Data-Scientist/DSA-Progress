class Solution:
    def compute_lps(self, s):
        if s == "":
            return 0
        lps = [0] * len(s)
        length, i = 0, 1
        # length = shows length of (longest prefix) that is also a suffix for current substring(to track new character after length)
        # lps[i] = shows length of longest prefix that is also a suffix for current substring(useful for algo)
        while (i < len(s)):
            # ((len+1)th/new character and current character) matched means increase the length
            if (s[i] == s[length]):
                length += 1
                lps[i] = length
                i += 1
            # not matched and if length is 0 already then lps[i] = 0
            elif (length == 0):
                lps[i] = 0
                i += 1
            # not matched and if length is not 0 means we need to decrease the length
            # length - 1 means last matched character index of (longest prefix) for which suffix is there in substring
            # It jumps to length = lps[length - 1] instead of length = 0
            else:
                length = lps[length-1]
        return lps
    def shortestPalindrome(self, s: str) -> str:
        s1 = s + '$' + s[::-1]
        lps = self.compute_lps(s1)
        return s[lps[-1]:][::-1] + s

print(Solution().shortestPalindrome("aacecaaa"))
print(Solution().shortestPalindrome("abcd"))