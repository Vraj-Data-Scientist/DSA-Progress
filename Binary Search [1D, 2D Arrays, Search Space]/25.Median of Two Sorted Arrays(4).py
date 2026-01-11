from typing import List

class Solution:
    def findMedianSortedArrays_brute(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        temp = []
        l = 0
        r = 0
        while (l < n1 and r < n2):
            if (nums1[l] <= nums2[r]):
                temp.append(nums1[l])
                l += 1
            else:
                temp.append(nums2[r])
                r += 1
        while (l < n1):
            temp.append(nums1[l])
            l += 1
        while (r < n2):
            temp.append(nums2[r])
            r += 1
        n = len(temp)
        median = 0
        if (n % 2 == 0):
            median = (temp[n//2] + temp[(n//2) - 1]) / 2.0
        else:
            median = temp[n//2]
        return median

    def findMedianSortedArrays_better(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        l = 0
        r = 0
        cnt = 0
        n = (n1 + n2)
        ind2 = n // 2
        ind1 = ind2 - 1
        ind1ele = -1
        ind2ele = -1
        while (l < n1 and r < n2):
            if (nums1[l] <= nums2[r]):
                if (cnt == ind1): ind1ele = nums1[l]
                if (cnt == ind2): ind2ele = nums1[l]
                cnt += 1
                l += 1
            else:
                if (cnt == ind1): ind1ele = nums2[r]
                if (cnt == ind2): ind2ele = nums2[r]
                cnt += 1
                r += 1
        while (l < n1):
            if (cnt == ind1): ind1ele = nums1[l]
            if (cnt == ind2): ind2ele = nums1[l]
            cnt += 1
            l += 1
        while (r < n2):
            if (cnt == ind1): ind1ele = nums2[r]
            if (cnt == ind2): ind2ele = nums2[r]
            cnt += 1
            r += 1
        median = 0
        if (n % 2 == 0):
            median = (ind1ele + ind2ele) / 2.0
        else:
            median = ind2ele
        return median

    def findMedianSortedArrays_optimal(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = (n1 + n2)
        if (n2 < n1):
            return Solution().findMedianSortedArrays_optimal(nums2, nums1)
        left = (n1 + n2 + 1) // 2
        low = 0
        high = n1
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
                if (n % 2 == 1):
                    return max(l1, l2)
                else:
                    return (max(l1, l2)+min(r1, r2))/2
            elif (l1 > r2):
                high = mid1 - 1
            elif (l2 > r1):
                low = mid1 + 1
        return -1




print(Solution().findMedianSortedArrays_brute([1,3], [2]))
print(Solution().findMedianSortedArrays_brute([1,2], [3,4]))
print(Solution().findMedianSortedArrays_better([1,3], [2]))
print(Solution().findMedianSortedArrays_better([1,2], [3,4]))
print(Solution().findMedianSortedArrays_optimal([1,3], [2]))
print(Solution().findMedianSortedArrays_optimal([1,2], [3,4]))