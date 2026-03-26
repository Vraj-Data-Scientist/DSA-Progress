from typing import List

class Solution:
    def transform(self, original, target):
        result = list(original)
        seen = set()
        for i in range(0, len(original)):
            char = original[i]
            if char in seen:
                continue
            seen.add(char)
            for j in range(0, len(original)):
                if (original[j] == char):
                    result[j] = target[i]
        return "".join(result)

    def isIsomorphic_brute(self, s: str, t: str) -> bool:
        s1 = self.transform(s, t)
        t1 = self.transform(t, s)
        return s1 == t and t1 == s


    def isIsomorphic(self, s: str, t: str) -> bool:
        n1= len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        dict1 = {}
        dict2 = {}
        for i in range(0, n1):
            if (s[i] in dict1 and dict1[s[i]] != t[i]):
                return False
            if (t[i] in dict2 and dict2[t[i]] != s[i]):
                return False
            dict1[s[i]] = t[i]
            dict2[t[i]] = s[i]
        return True

print(Solution().isIsomorphic_brute("paper", "title"))
print(Solution().isIsomorphic_brute("foo", "bar"))
print(Solution().isIsomorphic("paper", "title"))
print(Solution().isIsomorphic("foo", "bar"))


