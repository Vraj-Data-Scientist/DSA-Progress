class Solution:
    def is_palindrom(self, s):
        return s == s[::-1]

    def generate(self, ans, ds, s, start):
        if (start == len(s)):
            ans.append(ds)
            return
        for end in range(start+1, len(s)+1):
            if (self.is_palindrom(s[start:end])):
                self.generate(ans, ds + [s[start:end]], s, end)

    def palindrome_partition(self, s):
        ans = []
        ds = []
        self.generate(ans, ds, s, 0)
        return ans

print(Solution().palindrome_partition("aab"))
print(Solution().palindrome_partition("aabb"))
