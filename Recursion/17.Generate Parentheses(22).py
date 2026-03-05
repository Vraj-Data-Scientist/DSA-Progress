from typing import List

class Solution:
    def generate(self, ans, ds, n, open, close):
        if (len(ds) == 2*n):
            ans.append(ds)
            return
        if (open < n):
            self.generate(ans, ds+'(', n, open+1, close)
        if (close < open):
            self.generate(ans, ds+')', n, open, close+1)

    def combination(self, n):
        ans = []
        ds = ""
        self.generate(ans, ds, n, 0, 0)
        return ans

print(Solution().combination(3))