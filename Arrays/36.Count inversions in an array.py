from typing import List
from math import ceil

def merge_sort(arr:List[int], low:int, high:int) -> int:
    cnt = 0
    if (low >= high):
        return cnt
    mid = (low + high) // 2
    cnt += merge_sort(arr, low, mid)
    cnt += merge_sort(arr, mid+1, high)
    cnt += merge(arr, low, mid, high)
    return cnt

def merge(arr:List[int], low:int, mid:int, high:int) -> int:
    left = low
    right = mid + 1
    temp = []
    cnt = 0
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)
            right += 1
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i - low]
    return cnt

class Solution:
    def no_of_inversions_brute(self, arr:List[int]) -> int:
        n = len(arr)
        cnt = 0
        for i in range(0, n):
            for j in range(i+1, n):
                if (arr[i] > arr[j]):
                    cnt += 1
        return cnt

    def no_of_inversions_optimal(self, arr: List[int]) -> int:
        n = len(arr)
        return merge_sort(arr, 0 , n-1)

print(Solution().no_of_inversions_brute([2, 4, 1, 3, 5]))
print(Solution().no_of_inversions_brute([2, 3, 4, 5, 6]))
print(Solution().no_of_inversions_brute([10, 10, 10]))
print(Solution().no_of_inversions_optimal([2, 4, 1, 3, 5]))
print(Solution().no_of_inversions_optimal([2, 3, 4, 5, 6]))
print(Solution().no_of_inversions_optimal([10, 10, 10]))
