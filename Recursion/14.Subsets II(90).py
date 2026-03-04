from typing import List

class Solution:
    def find_subset(self, ind, arr, ans, ds):
        ans.append(list(ds))
        for i in range(ind, len(arr)):
            if (i > ind and arr[i] == arr[i-1]):
                continue
            ds.append(arr[i])
            self.find_subset(i+1, arr, ans, ds)
            ds.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        nums.sort()
        self.find_subset(0, nums, ans, ds)
        return ans

print(Solution().subsetsWithDup([1,2,2]))
print(Solution().subsetsWithDup([0]))