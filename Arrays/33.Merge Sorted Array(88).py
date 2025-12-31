from typing import List

class Solution:
    def merge_brute(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        l = 0
        r = 0
        while (r < n):
            if (l < (m+r) and nums1[l] < nums2[r]):
                l += 1
            else:
                for i in range(m+r-1, l-1, -1):
                    nums1[i+1] = nums1[i]
                nums1[l] = nums2[r]
                r += 1
                l += 1
        return nums1

    def merge_optimal(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        l = m - 1
        r = n - 1
        index = m + n - 1
        while (r >= 0 and l >= 0):
            if (nums1[l] > nums2[r]):
                nums1[index] = nums1[l]
                l -= 1
            else:
                nums1[index] = nums2[r]
                r -= 1
            index -= 1
        while (r >= 0):
            nums1[index] = nums2[r]
            r -= 1
            index -= 1
        while (l >= 0):
            nums1[index] = nums1[l]
            l -= 1
            index -= 1
        return nums1


print(Solution().merge_brute([1,2,3,0,0,0], 3, [2,5,6], 3))
print(Solution().merge_brute([0], 0, [1], 1))
print(Solution().merge_brute([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))
print(Solution().merge_optimal([1,2,3,0,0,0], 3, [2,5,6], 3))
print(Solution().merge_optimal([0], 0, [1], 1))
print(Solution().merge_optimal([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))