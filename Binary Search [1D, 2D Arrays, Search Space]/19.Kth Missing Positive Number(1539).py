from typing import List

def binary_search(nums:List[int], target:int):
    n = len(nums)
    low = 0
    high = n - 1
    while (low <= high):
        mid = (low+high) // 2
        if (nums[mid] == target):
            return True
        elif (nums[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    return False

class Solution:
    def findKthPositive_brute(self, arr: List[int], k: int) -> int:
        n = len(arr)
        position = 0
        i = 1
        while(1):
            if (binary_search(arr, i) == True):
                i += 1
            else:
                position += 1
                if (position == k):
                    return i
                i += 1

    def findKthPositive_better(self, arr: List[int], k: int):
        n = len(arr)
        for i in range(0, n):
            if (arr[i] <= k):
                k += 1
            else:
                break
        return k

    def findKthPositive_optimal(self, arr: List[int], k: int):
        n = len(arr)
        low = 0
        high = n - 1
        while (low <= high):
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)
            if (missing < k):
                low = mid + 1
            else:
                high = mid - 1
        return k + high + 1

print(Solution().findKthPositive_brute([2,3,4,7,11], 5))
print(Solution().findKthPositive_brute([1,2,3,4], 2))
print(Solution().findKthPositive_better([2,3,4,7,11], 5))
print(Solution().findKthPositive_better([1,2,3,4], 2))
print(Solution().findKthPositive_optimal([2,3,4,7,11], 5))
print(Solution().findKthPositive_optimal([1,2,3,4], 2))