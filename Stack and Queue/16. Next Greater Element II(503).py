from typing import List

class Solution:
    def nextGreaterElements_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        for i in range(0, n):
            for j in range(i+1, i+n):
                index = j % n
                if (nums[index] > nums[i]):
                    nge[i] = nums[index]
                    break
        return nge

    def nextGreaterElements_optimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        st = []
        for i in range(2*n, -1, -1):
            while (st and st[-1] <= nums[i % n]):
                st.pop()
            if (i < n):
                nge[i] = -1 if not st else st[-1]
            st.append(nums[i % n])
        return nge

print(Solution().nextGreaterElements_brute([1,2,1]))
print(Solution().nextGreaterElements_brute([1,2,1]))
print(Solution().nextGreaterElements_optimal([1,2,3,4,3]))
print(Solution().nextGreaterElements_optimal([1,2,3,4,3]))