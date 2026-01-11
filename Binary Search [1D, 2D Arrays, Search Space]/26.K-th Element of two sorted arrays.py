from typing import List

class Solution:
    def find_kth_ele_in_SortedArrays_optimal(self, nums1: List[int], nums2: List[int], k : int) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = (n1 + n2)
        if (n2 < n1):
            return Solution().find_kth_ele_in_SortedArrays_optimal(nums2, nums1, k)
        left = k
        low = max(0, k-n2)
        high = min(k, n1)
        while (low <= high):
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            if (mid1 < n1): r1 = nums1[mid1]
            if (mid2 < n2): r2 = nums2[mid2]
            if (mid1 - 1 >= 0): l1 = nums1[mid1 - 1]
            if (mid2 - 1 >= 0): l2 = nums2[mid2 - 1]

            if (l1 <= r2 and l2 <= r1):
                return max(l1, l2)
            elif (l1 > r2):
                high = mid1 - 1
            elif (l2 > r1):
                low = mid1 + 1
        return -1

print(Solution().find_kth_ele_in_SortedArrays_optimal([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))
print(Solution().find_kth_ele_in_SortedArrays_optimal([100, 112, 256, 349, 770],[72, 86, 113, 119, 265, 445, 892], 7 ))