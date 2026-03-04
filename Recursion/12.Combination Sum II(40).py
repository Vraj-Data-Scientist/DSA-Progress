from typing import List

class Solution:
    def find_combi(self, ind, arr, ds, ans, target):
        if (ind == len(arr)):
            if (target == 0):
                ans.add(tuple(sorted(ds)))
            return
        if (arr[ind] <= target):  # to stop taking
            ds.append(arr[ind])
            self.find_combi(ind, arr, ds, ans, target - arr[ind])
            ds.pop()
        self.find_combi(ind + 1, arr, ds, ans, target)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        ds = []
        self.find_combi(0, candidates, ds, ans, target)
        l1 = [list(tup) for tup in ans]
        return l1

    def find_combi2(self, ind, arr, ds, ans, target):
        if (ind == len(arr)):
            if (target == 0):
                ans.add(tuple(sorted(ds)))
            return
        ds.append(arr[ind])
        self.find_combi2(ind + 1, arr, ds, ans, target - arr[ind])
        ds.pop()
        self.find_combi2(ind + 1, arr, ds, ans, target)

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        ds = []
        self.find_combi2(0, candidates, ds, ans, target)
        l1 = [list(tup) for tup in ans]
        return l1

    def combinationSum4(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        ds = []
        self.find_combi2(0, candidates, ds, ans, target)
        l1 = [list(tup) for tup in ans]
        l1.sort()
        return l1

    def findCombination(self, ind, arr, target, ds, ans):
        if (target == 0):
            ans.append(list(ds))
            return
        for i in range(ind, len(arr)):
            if (i > ind and arr[i] == arr[i-1]):
                continue
            if (arr[i] > target):
                break
            ds.append(arr[i])
            self.findCombination(i+1, arr, target - arr[i], ds, ans)
            ds.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        candidates.sort()
        self.findCombination(0, candidates, target, ds, ans)
        return ans


print(Solution().combinationSum2([2, 3, 6, 7], 7))
print(Solution().combinationSum2([2, 1, 3, 1, 1], 2))
print(Solution().combinationSum3([2, 3, 6, 7], 7))
print(Solution().combinationSum3([2, 1, 3, 1, 1], 2))
print(Solution().combinationSum3([2, 1, 3, 1, 1, 1], 3))  # set unordered
print(Solution().combinationSum4([2, 1, 3, 1, 1, 1], 3))
print(Solution().combinationSum4([10,1,2,7,6,1,5], 8))
print(Solution().combinationSum([10,1,2,7,6,1,5], 8))
