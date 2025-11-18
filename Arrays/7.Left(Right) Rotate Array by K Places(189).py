from typing import List

class Solution:
    def rotate_brute(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        temp = []
        k = k % n
        for i in range(n-k, n):
            temp.append(nums[i])
        for i in range(n-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(0, k):
            nums[i] = temp[i]
        return nums

    def reverse_array(self, array: List[int], start: int, end: int):
        while (start < end):
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
    def rotate_optimal(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        Solution().reverse_array(nums, 0, n-k-1)
        Solution().reverse_array(nums, n-k, n-1)
        Solution().reverse_array(nums, 0, n-1)
        return nums

print(Solution().rotate_brute([1,2,3,4,5,6,7], 3))
print(Solution().rotate_optimal([1,2,3,4,5,6,7], 3))
