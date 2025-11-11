class Solution(object):

    def longestOnes_brute(self, nums, k):
        n = len(nums)
        max_len = 0
        for i in range(0, n):
            cnt_0 = 0
            for j in range(i, n):
                if (nums[j] == 0):
                    cnt_0 += 1
                if (cnt_0 > k):
                    break
                if (cnt_0 <= k):
                    max_len = max(max_len, j-i+1)
        return max_len

    def longestOnes_better(self, nums, k):
        n = len(nums)
        max_len = 0
        l = 0
        r = 0
        cnt_0 = 0
        while (r < n):
            if (nums[r] == 0):
                cnt_0 += 1
            while (cnt_0 > k):
                if (nums[l] == 0):
                    cnt_0 -= 1
                l += 1
            if (cnt_0 <= k):
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

    def longestOnes_optimal(self, nums, k):
        n = len(nums)
        max_len = 0
        l = 0
        r = 0
        cnt_0 = 0
        while (r < n):
            if (nums[r] == 0):
                cnt_0 += 1
            if (cnt_0 > k):
                if (nums[l] == 0):
                    cnt_0 -= 1
                l += 1
            if (cnt_0 <= k):
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

print(Solution().longestOnes_brute([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(Solution().longestOnes_better([1,1,1,0,0,0,1,1,1,1,0],2))
print(Solution().longestOnes_optimal([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))

