from typing import List

class Solution:
    def find_subset_sums(self, i, arr, ans, sum):
        n = len(arr)
        if (i >= n):
            ans.append(sum)
            return
        self.find_subset_sums(i+1, arr, ans, sum+arr[i])
        self.find_subset_sums(i+1, arr, ans, sum)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.find_subset_sums(0, nums, ans, 0)
        ans.sort()
        return ans

print(Solution().subsets([5,2,1]))


