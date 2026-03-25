from typing import List

class Solution:
    def starts_with(self, str, prefix):
        if len(prefix) > len(str):
            return False
        for i in range(0, len(prefix)):
            if str[i] != prefix[i]:
                return False
        return True

    def longestCommonPrefix_brute(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        n = len(first)
        prefix = ""
        for i in range(0, n):
            prefix = prefix + first[i]
            for word in strs:
                if not word.startswith(prefix):
                    return first[:i]
        return first

    def longestCommonPrefix_better(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        n = len(first)
        for i in range(0, n):
            char = first[i]
            for word in strs:
                if (i > (len(word)-1) or word[i] != char):
                    return first[:i]
        return first

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        n1 = len(first)
        n2 = len(last)
        for i in range(0, min(n1, n2)):
            if (first[i] != last[i]):
                return first[:i]
        return first

print(Solution().starts_with("flow", "f"))
print(Solution().starts_with("flow", "fl"))
print(Solution().starts_with("flow", "flo"))
print(Solution().starts_with("flow", "flow"))
print(Solution().starts_with("flow", "flowe"))
print(Solution().longestCommonPrefix_brute(["flower","flow","flight"]))
print(Solution().longestCommonPrefix_brute(["dog","racecar","car"]))
print(Solution().longestCommonPrefix_better(["flower","flow","flight"]))
print(Solution().longestCommonPrefix_better(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
