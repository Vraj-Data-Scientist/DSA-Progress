class Solution:
    def longestPalindrome_brute(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        max_len = 0
        max_str = ''
        for i in range(0, n):
            for j in range(i, n):
                if (s[i:j+1] == s[i:j+1][::-1] and j-i+1 > max_len):
                    max_len = max(max_len, j-i+1)
                    max_str = s[i:j+1]
        return max_str

    def longestPalindrome_better(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        max_len = 0
        max_str = ''
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(0, n):
            for j in range(0, i+1):
                if (s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1])):
                    dp[j][i] = True
                    if (i-j+1 > max_len):
                        max_len = i-j+1
                        max_str = s[j:i+1]
        return max_str

    def expand(self, left, right, s):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome_better_2(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        max_len = 0
        max_str = ''
        for i in range(0, n):
            odd_palindrome = self.expand(i,i,s)
            even_palindrome = self.expand(i,i+1,s)
            if len(odd_palindrome) > max_len:
                max_str = odd_palindrome
                max_len = len(odd_palindrome)
            if len(even_palindrome) > max_len:
                max_str = even_palindrome
                max_len = len(even_palindrome)
        return max_str

    def longestPalindrome_optimal(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        max_len = 0
        max_str = ''
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
            if (dp[i] > max_len):
                max_len = dp[i]
                max_str = s[i-dp[i]:i+dp[i]+1]
        max_str = max_str.replace('#','')
        return max_str





print(Solution().longestPalindrome_brute('babad'))
print(Solution().longestPalindrome_better('babad'))
print(Solution().longestPalindrome_better_2('babad'))
print(Solution().longestPalindrome_optimal('babad'))
