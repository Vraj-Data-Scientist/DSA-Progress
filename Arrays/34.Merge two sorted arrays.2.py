from typing import List

class Solution:
    def merge_brute(self, nums1: List[int], nums2: List[int]) -> tuple[List[int], List[int]]:
        m = len(nums1)
        n = len(nums2)
        l = 0
        r = 0
        index = 0
        answer = [0 for i in range((m+n))]
        while (l < m and r < n):
            if (nums1[l] <= nums2[r]):
                answer[index] = nums1[l]
                l += 1
            else:
                answer[index] = nums2[r]
                r += 1
            index += 1
        while (l < m):
            answer[index] = nums1[l]
            l += 1
            index += 1
        while (r < n):
            answer[index] = nums2[r]
            r += 1
            index += 1

        k = len(answer)
        for i in range(0, k):
            if (i < m):
                nums1[i] = answer[i]
            else:
                nums2[i - m] = answer[i]
        return (nums1, nums2)

    def merge_optimal_1(self, nums1: List[int], nums2: List[int]) -> tuple[List[int], List[int]]:
        m = len(nums1)
        n = len(nums2)
        l = m - 1
        r = 0
        while (l >= 0 and r < n):
            if (nums1[l] > nums2[r]):
                nums1[l], nums2[r] = nums2[r], nums1[l]
                l -= 1
                r += 1
            else:
                break
        nums1.sort()
        nums2.sort()
        return nums1, nums2

    def merge_optimal_2(self, nums1: List[int], nums2: List[int]) -> tuple[List[int], List[int]]:
        m = len(nums1)
        n = len(nums2)
        l = m + n
        gap = (l // 2) + (l % 2)
        while (gap > 0):
            left = 0
            right = left + gap
            while (right < l):
                if (left < m and right >= m):
                    if (nums1[left] > nums2[right - m]):
                        nums1[left], nums2[right - m] = nums2[right - m], nums1[left]
                elif (left >= m):
                    if (nums2[left - m] > nums2[right - m]):
                        nums2[left - m], nums2[right - m] = nums2[right - m], nums2[left - m]
                else:
                    if (nums1[left] > nums1[right]):
                        nums1[left], nums1[right] = nums1[right], nums1[left]
                left += 1
                right += 1
            if (gap == 1):
                break
            gap = (gap // 2) + (gap % 2)
        return nums1, nums2



print(Solution().merge_brute([1, 3, 5, 7], [2, 4, 6, 8]))
print(Solution().merge_brute([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))
print(Solution().merge_optimal_1([1, 3, 5, 7], [2, 4, 6, 8]))
print(Solution().merge_optimal_1([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))
print(Solution().merge_optimal_2([1, 3, 5, 7], [2, 4, 6, 8]))
print(Solution().merge_optimal_2([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))


