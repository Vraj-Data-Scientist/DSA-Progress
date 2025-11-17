class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(1,n):
            if (nums[i] >= nums[i-1]):
                pass
            else:
                return False
        return True

print(Solution().check([3,4,5,1,2]))