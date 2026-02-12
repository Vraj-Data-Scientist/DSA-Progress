from typing import List

class Solution:
    def nextGreaterElement_brute(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        nge = [-1]*n
        for i in range(0, n):
            for j in range(0, m):
                if (nums1[i] == nums2[j]):
                    index = j
                    break
            for j in range(index+1, m):
                if (nums1[i] < nums2[j]):
                    nge[i] = nums2[j]
                    break
        return nge

    def nextGreaterElement_optimal(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        nge = [-1]*n
        st = []
        dict1 = {}
        for i in range(m-1, -1, -1):
            while (st and st[-1] <= nums2[i]):
                st.pop()
            dict1[nums2[i]] = -1 if (not st) else st[-1]
            st.append(nums2[i])
        for i in range(0, n):
            nge[i] = dict1[nums1[i]]
        return nge

print(Solution().nextGreaterElement_brute([4,1,2], [1,3,4,2]))
print(Solution().nextGreaterElement_brute([2,4], [1,2,3,4]))
print(Solution().nextGreaterElement_optimal([4,1,2], [1,3,4,2]))
print(Solution().nextGreaterElement_optimal([2,4], [1,2,3,4]))

