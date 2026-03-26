class Solution:
    def isAnagram_brute(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if (n1 != n2):
            return False
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        return s1 == t1

    def isAnagram_better(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if (n1 != n2):
            return False
        cnt = [0] * 26
        for char in s:
            cnt[ord(char) - ord('a')] += 1
        for char in t:
            if (cnt[ord(char) - ord('a')] == 0):
                return False
            cnt[ord(char) - ord('a')] -= 1
        return True

    def isAnagram_optimal(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if (n1 != n2):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(0, n1):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        return s_dict == t_dict

print(Solution().isAnagram_brute("anagram", "nagaram"))
print(Solution().isAnagram_better("anagram", "nagaram"))
print(Solution().isAnagram_optimal("anagram", "nagaram"))