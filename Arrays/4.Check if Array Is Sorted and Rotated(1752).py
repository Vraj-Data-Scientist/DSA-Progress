class Solution(object):
    def check(self, nums):
        n = len(nums)
        cnt = 0
        for i in range(0,n):
            if (nums[i] > nums[(i + 1) % n]):
                cnt += 1
            if (cnt > 1):
                return False
        return True

print(Solution().check([3,4,5,1,2]))
print(Solution().check([2,1,3,4]))
print(Solution().check([1,2,3]))