from typing import List

class Solution:
    def union_sortedarray_brute(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        result = []
        set1 = set()
        for i in range(0, n1):
            set1.add(nums1[i])
        for j in range(0, n2):
            set1.add(nums2[j])
        for item in set1:
            result.append(item)
        result.sort()
        return result

    def union_sortedarray_optimal(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        result = []
        while (i < n1 and j < n2):
            if (nums1[i] == nums2[j]):
                if (not result or result[-1] != nums1[i]):
                    result.append(nums1[i])
                i += 1
                j += 1
            elif (nums1[i] < nums2[j]):
                if (not result or result[-1] != nums1[i]):
                    result.append(nums1[i])
                i += 1
            else:
                if (not result or result[-1] != nums2[j]):
                    result.append(nums2[j])
                j += 1
        while (i < n1):
            if (not result or result[-1] != nums1[i]):
                result.append(nums1[i])
            i += 1
        while (j < n2):
            if (not result or result[-1] != nums2[j]):
                result.append(nums2[j])
            j += 1
        return result

print(Solution().union_sortedarray_optimal([3, 5, 10, 10, 10, 15, 15, 20], [5, 10, 10, 15, 30]))
print(Solution().union_sortedarray_optimal([3, 5, 10, 10], [5, 10, 10]))
print(Solution().union_sortedarray_brute([3, 5, 10, 10, 10, 15, 15, 20], [5, 10, 10, 15, 30]))
print(Solution().union_sortedarray_brute([3, 5, 10, 10], [5, 10, 10]))

