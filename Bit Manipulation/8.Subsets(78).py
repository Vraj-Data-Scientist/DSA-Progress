from typing import List

class Solution:
    def solve(self, nums, i, ds, res):
        n = len(nums)
        if (i == n):
            res.append(list(ds))
            return
        ds.append(nums[i])
        self.solve(nums, i+1, ds, res)
        ds.remove(nums[i])
        self.solve(nums, i+1, ds, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds = []
        res = []
        self.solve(nums, 0, ds, res)
        return res

    def subsets_bit_manipulation(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = (1 << n)
        res = []
        for i in range(0, subset):
            ds = []
            for j in range(0, n):
                if (i & (1 << j)):
                    ds.append(nums[j])
            res.append(ds)
        return res

print(Solution().subsets([1,2,3]))
print(Solution().subsets_bit_manipulation([1,2,3]))
