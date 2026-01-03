class Solution:
    def findFloor(self, arr, x):
        n = len(arr)
        low = 0
        high = n-1
        ans = -1
        while (low <= high):
            mid = (low + high) // 2
            if (arr[mid] <= x):
                ans = mid
                low = mid + 1
            elif (arr[mid] > x):
                high = mid - 1
        return ans

    def findCeil(self, arr, x):
        n = len(arr)
        low = 0
        high = n-1
        ans = -1
        while (low <= high):
            mid = (low + high) // 2
            if (arr[mid] < x):
                low = mid + 1
            elif (arr[mid] >= x):
                ans = mid
                high = mid - 1
        return ans

print(Solution().findFloor([1, 2, 8, 10, 10, 12, 19], 5))
print(Solution().findFloor([1, 2, 8, 10, 10, 12, 19], 11))
print(Solution().findFloor([1, 2, 8, 10, 10, 12, 19], 0))
print(Solution().findCeil([1, 2, 8, 10, 11, 12, 19], 5))
print(Solution().findCeil([1, 2, 8, 10, 11, 12, 19], 20))
print(Solution().findCeil([1, 1, 2, 8, 10, 11, 12, 19], 0))