from typing import List

class Solution:
    def find_combination(self, k, target, ds, ans, element):
        if (len(ds) == k and target == 0):
            ans.append(list(ds))
            return
        if (len(ds) > k or target < 0):
            return
        for i in range(element, 10):
            if (i <= target):
                ds.append(i)
                self.find_combination(k, target-i, ds, ans, i+1)
                ds.pop()
            else:
                break

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ds = []
        ans = []
        self.find_combination(k, n, ds, ans, 1)
        return ans

print(Solution().combinationSum3(3, 7))