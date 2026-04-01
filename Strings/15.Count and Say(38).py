class Solution:
    def RLE(self, s):
        cnt = 1
        result = ''
        for i in range(1, len(s)):
            if (s[i] == s[i-1]):
                cnt += 1
            else:
                result += (str(cnt) + s[i-1])
                cnt = 1
        result += (str(cnt) + s[-1])
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.RLE(self.countAndSay(n-1))

    def countAndSay_iterative(self, n: int) -> str:
        result = '1'
        for i in range(0, n-1):
            result = self.RLE(result)
        return result

print(Solution().countAndSay(5))
print(Solution().countAndSay_iterative(5))

