class Solution:
    def countSubstrings_brute(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        cnt = 0
        for i in range(0, n):
            for j in range(i, n):
                if (s[i:j+1] == s[i:j+1][::-1]):
                    cnt += 1
        return cnt

    def countSubstrings_better(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        cnt = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(0, n):
            for j in range(0, i+1):
                if (s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1])):
                    dp[j][i] = True
                    cnt += 1
        return cnt

    def expand(self, left, right, s):
        cnt = 0
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            cnt += 1
        return cnt

    def countSubstrings_better_2(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        cnt = 0
        for i in range(0, n):
            cnt += self.expand(i,i,s)
            cnt += self.expand(i,i+1,s)
        return cnt

    def countSubstrings_optimal(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        cnt = 0
        center = 0
        right = 0
        dp = [0 for _ in range(0, n)]
        for i in range(0, n):
            if (i < right):
                dp[i] = min(right-i, dp[2*center-i])
            while (i+dp[i]+1 < len(s) and
                   i-dp[i]-1 >= 0 and
                   s[i-dp[i]-1] == s[i+dp[i]+1]):
                dp[i] += 1
            if (i+dp[i] > right):
                center = i
                right = i+dp[i]
            cnt += (dp[i] + 1) // 2
        return cnt

print(Solution().countSubstrings_brute("abc"))
print(Solution().countSubstrings_better("abc"))
print(Solution().countSubstrings_better_2("abc"))
print(Solution().countSubstrings_optimal("abc"))
