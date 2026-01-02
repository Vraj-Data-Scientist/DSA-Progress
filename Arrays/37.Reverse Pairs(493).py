from typing import List

def merge_sort(arr:List[int], low:int, high:int):
    cnt = 0
    if (low >= high):
        return cnt
    mid = (low + high) // 2
    cnt += merge_sort(arr, low, mid)
    cnt += merge_sort(arr, mid+1, high)
    cnt += count_pairs(arr, low, mid, high)
    merge(arr, low, mid, high)
    return cnt

def merge(arr:List[int], low:int, mid:int, high:int):
    left = low
    right = mid + 1
    temp = []
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i - low]

def count_pairs(arr:List[int], low:int, mid:int, high:int):
    right = mid + 1
    cnt = 0
    for i in range(low, mid+1):
        while (right <= high and arr[i] > 2*arr[right]):
            right += 1
        cnt += (right - (mid + 1))
    return cnt

class Solution:
    def reversePairs_brute(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0, n):
            for j in range(i+1, n):
                if (nums[i] > 2*nums[j]):
                    cnt += 1
        return cnt

    def reversePairs_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        return merge_sort(nums, 0, n-1)


print(Solution().reversePairs_brute([1,3,2,3,1]))
print(Solution().reversePairs_brute([2,4,3,5,1]))
print(Solution().reversePairs_optimal([1,3,2,3,1]))
print(Solution().reversePairs_optimal([2,4,3,5,1]))


