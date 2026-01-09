from typing import List

def count_student(arr:List[int], max_pages):
    n = len(arr)
    student = 1
    pages_student = 0
    for i in range(0, n):
        if (pages_student + arr[i] <= max_pages):
            pages_student += arr[i]
        else:
            student += 1
            pages_student = arr[i]
    return student

print(count_student([25, 46, 28, 49, 24], 49))
print(count_student([25, 46, 28, 49, 24], 70))
print(count_student([25, 46, 28, 49, 24], 71))

class Solution:
    def findPages_brute(self, arr:List[int], n:int, m:int):
        if (m > n):
            return -1
        for i in range(max(arr), sum(arr)+1):
            if (count_student(arr, i) == m):
                return i
        return max(arr)

    def findPages_optimal(self, arr:List[int], n:int, m:int):
        if (m > n):
            return -1
        low = max(arr)
        high = sum(arr)
        while(low <= high):
            mid = (low+high) // 2
            if (count_student(arr, mid) > m):
                low = mid + 1
            else:
                high = mid - 1
        return low


print(Solution().findPages_brute([25, 46, 28, 49, 24], 5, 4))
print(Solution().findPages_brute([12, 34, 67, 90], 4, 2))
print(Solution().findPages_optimal([25, 46, 28, 49, 24], 5, 4))
print(Solution().findPages_optimal([12, 34, 67, 90], 4, 2))


