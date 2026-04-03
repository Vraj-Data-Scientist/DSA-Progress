class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        cnt = 1
        source = a
        while (len(source) < len(b)):
            source = source + a
            cnt += 1
        if (source.find(b) != -1):
            return cnt
        source = source + a
        cnt += 1
        if (source.find(b) != -1):
            return cnt
        return -1

print(Solution().repeatedStringMatch("abcd", "cdabcdab"))
print(Solution().repeatedStringMatch("a", "aa"))