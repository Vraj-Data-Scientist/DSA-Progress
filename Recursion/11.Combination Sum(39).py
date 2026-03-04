from typing import List

class Solution:
    def find_combi(self, ind, arr, ds, ans, target):
        if (ind == len(arr)):
            if (target == 0):
                ans.append(list(ds))
            return
        if (arr[ind] <= target):               #to stop taking
            ds.append(arr[ind])
            self.find_combi(ind, arr, ds, ans, target - arr[ind])
            ds.pop()
        self.find_combi(ind+1, arr, ds, ans, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        self.find_combi(0, candidates, ds, ans, target)
        return ans

print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([1,1,3,2,1], 2))




