from typing import List

class Solution:
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def generate(self, ans, ds, digits, index):
        if (len(digits) == index):
            ans.append(ds)
            return
        s = self.map[int(digits[index])]
        print(s)
        for char in s:
            self.generate(ans, ds+char, digits, index+1)

    def letterCombinations(self, digits: str) -> List[str]:
        ds = ""
        ans = []
        if not digits:
            return ans
        self.generate(ans, ds, digits, 0)
        return ans

print(Solution().letterCombinations("34"))