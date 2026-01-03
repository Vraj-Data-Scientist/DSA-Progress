class Solution:
    def upperBound_1(self, arr, target):
        n = len(arr)
        low = 0
        high = n-1
        while (low <= high):
            if (low == high and arr[low] > target):
                return low
            mid = (low + high) // 2
            if (arr[mid] <= target):
                low = mid + 1
            elif (arr[mid] > target):
                high = mid
        return n

    def upperBound_2(self, arr, target):
        n = len(arr)
        low = 0
        high = n-1
        ans = n
        while (low <= high):
            mid = (low + high) // 2
            if (arr[mid] <= target):
                low = mid + 1
            elif (arr[mid] > target):
                ans = mid
                high = mid - 1
        return ans

print(Solution().upperBound_1([2, 3, 7, 10, 11, 11, 25], 9))
print(Solution().upperBound_1([2, 3, 7, 10, 11, 11, 25], 100))
print(Solution().upperBound_2([2, 3, 7, 10, 11, 11, 25], 9))
print(Solution().upperBound_2([2, 3, 7, 10, 11, 11, 25], 100))