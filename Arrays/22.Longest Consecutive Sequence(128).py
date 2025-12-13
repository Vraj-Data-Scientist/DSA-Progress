from typing import List

class Solution:
    def search(self, a, key) -> bool:
        for i in range(0, len(a)):
            if (a[i] == key):
                return True
        return False
    def longestConsecutive_brute(self, nums: List[int]) -> int:
        max_len = 0
        n = len(nums)
        for i in range(0, n):
            x = nums[i]
            cnt = 1
            while((Solution().search(nums, x+1)) == True):
                x = x+1
                cnt += 1
            max_len = max(max_len, cnt)
        return max_len

    def longestConsecutive_better(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_len = 1
        cnt = 0
        last_smaller = float('-inf')
        for i in range(0,n):
            if (nums[i] - 1 == last_smaller):
                last_smaller = nums[i]
                cnt += 1
            elif (nums[i] != last_smaller):
                cnt = 1
                last_smaller = nums[i]
            max_len = max(max_len, cnt)
        return max_len

    def longestConsecutive_optimal(self, nums: List[int]) -> int:
        set1 = set()
        n = len(nums)
        max_len = 0
        for i in range(0, n):
            set1.add(nums[i])
        for item in set1:
            if ((item-1) not in set1):
                x = item
                cnt = 1
                while((x + 1) in set1):
                    x += 1
                    cnt += 1
                max_len = max(max_len, cnt)
        return max_len

print(Solution().longestConsecutive_brute([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive_brute([100,4,200,1,3,2]))
print(Solution().longestConsecutive_brute([1,0,1,2]))
print(Solution().longestConsecutive_better([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive_better([100,4,200,1,3,2]))
print(Solution().longestConsecutive_better([1,0,1,2]))
print(Solution().longestConsecutive_optimal([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive_optimal([100,4,200,1,3,2]))
print(Solution().longestConsecutive_optimal([1,0,1,2]))