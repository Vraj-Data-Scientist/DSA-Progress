class Solution:
    def rotateString_brute(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if (m != n):
            return False
        for _ in range(0, n):
            s = s[1:] + s[0]
            if (s == goal):
                return True
        return False

    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if (m != n):
            return False
        s1 = s + s
        return s1.find(goal) != -1

    def my_find(self, str, substring):
        n = len(str)
        m = len(substring)
        if m > n:
            return -1
        for i in range(0, n-m+1):
            if (str[i:i+m] == substring):
                return i
        return -1

print(Solution().rotateString_brute("abcde", "cdeab"))
print(Solution().rotateString_brute("abcde", "abced"))
print(Solution().rotateString("abcde", "cdeab"))
print(Solution().rotateString("abcde", "abced"))
print(Solution().my_find("abc", "c"))
print(Solution().my_find("abc", "bcd"))

