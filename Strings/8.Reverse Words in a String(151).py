from typing import List

class Solution:
    def my_split(self, s):
        n = len(s)
        if not s:
            return []
        words = []
        i = 0
        while (i < n):
            while (i < n and s[i].isspace()):
                i += 1
            if (i == n):
                break
            start = i
            while (i < n and not s[i].isspace()):
                i += 1
            words.append(s[start:i])
        return words

    def reverseWords_brute(self, s: str) -> str:
        n = len(s)
        words = s.split()
        res = []
        for i in range(len(words)-1, -1, -1):
            res.append(words[i])
            if (i != 0):
                res.append(" ")
        return "".join(res)

    def reverseWords_better(self, s: str) -> str:
        n = len(s)
        words = s.split()
        left, right = 0, len(words)-1
        while (left < right):
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)

    def reverseWords_brute_2(self, s: str) -> str:
        n = len(s)
        s = s[::-1]
        ans = ''
        i = 0
        while (i < n):
            word = ''
            while (i < n and s[i] != " "):
                word += s[i]
                i += 1
            word = word[::-1]
            if (len(word) > 0):
                ans += " " + word
            i += 1    #skip space
        return ans[1:]

print(Solution().my_split("the sky is blue"))
print(Solution().my_split("  hello world  "))
print(Solution().my_split("a good   example"))
print(Solution().reverseWords_brute("the sky is blue"))
print(Solution().reverseWords_brute("  hello world  "))
print(Solution().reverseWords_brute("a good   example"))
print(Solution().reverseWords_better("the sky is blue"))
print(Solution().reverseWords_better("  hello world  "))
print(Solution().reverseWords_better("a good   example"))
print(Solution().reverseWords_brute_2("the sky is blue"))
print(Solution().reverseWords_brute_2("  hello world  "))
print(Solution().reverseWords_brute_2("a good   example"))
