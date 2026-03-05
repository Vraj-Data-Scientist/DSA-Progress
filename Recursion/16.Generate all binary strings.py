from typing import List

class Solution:
    def generate(self, ans, ds, n):
        if (len(ds) == n):
            ans.append(ds)
            return
        self.generate(ans, ds + "0", n)
        if (not ds or ds[-1] != "1"):
            self.generate(ans, ds + "1", n)

    def combination(self, n):
        ans = []
        ds = ""
        self.generate(ans, ds, n)
        return ans

print(Solution().combination(3))