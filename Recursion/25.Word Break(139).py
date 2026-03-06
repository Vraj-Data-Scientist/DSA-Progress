from typing import List

class Solution:
    def solve_brute(self, s, wordDict, start):
        if (start == len(s)):
            return True
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if (word in wordDict):
                if (self.solve_brute(s, wordDict, end) == True):
                    return True
        return False

    def wordBreak_brute(self, s: str, wordDict: List[str]) -> bool:
        return self.solve_brute(s, wordDict, 0)

    def solve(self, s, wordDict, start, dp):
        if (start == len(s)):
            return True
        if (dp[start] != -1):
            return dp[start] == 1
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if (word in wordDict):
                if (self.solve(s, wordDict, end, dp) == True):
                    dp[start] = 1
                    return True
        dp[start] = 0
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * (len(s) + 1)
        return self.solve(s, wordDict, 0, dp)

print(Solution().wordBreak_brute("leetcode",["leet","code"]))
print(Solution().wordBreak_brute("applepenapple",["apple","pen"]))
print(Solution().wordBreak_brute("catsandog",["cats","dog","sand","and","cat"]))
print(Solution().wordBreak("leetcode",["leet","code"]))
print(Solution().wordBreak("applepenapple",["apple","pen"]))
print(Solution().wordBreak("catsandog",["cats","dog","sand","and","cat"]))
