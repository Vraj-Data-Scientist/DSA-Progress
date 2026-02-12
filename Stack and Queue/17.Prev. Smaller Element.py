from typing import List

class Solution:
    def prevSmallerElement_brute(self, nums1: List[int]) -> List[int]:
        n = len(nums1)
        pse = [-1]*n
        for i in range(0, n):
            for j in range(i-1, -1, -1):
                if (nums1[j] < nums1[i]):
                    pse[i] = nums1[j]
                    break
        return pse

    def prevSmallerElement_optimal(self, nums1: List[int]) -> List[int]:
        n = len(nums1)
        pse = [-1]*n
        st = []
        for i in range(0, n):
            while (st and st[-1] >= nums1[i]):
                st.pop()
            pse[i] = -1 if (not st) else st[-1]
            st.append(nums1[i])
        return pse

print(Solution().prevSmallerElement_brute([4,5,2,10,8]))
print(Solution().prevSmallerElement_optimal([4,5,2,10,8]))




