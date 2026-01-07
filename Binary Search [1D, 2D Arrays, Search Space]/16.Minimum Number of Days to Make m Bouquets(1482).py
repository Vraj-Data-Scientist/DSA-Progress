from typing import List

def bouquets_possible_or_not(nums:List[int], m:int, k:int, days:int) -> bool:
    n = len(nums)
    cnt = 0
    m1 = 0
    for i in range(0, n):
        if (nums[i] <= days):
            cnt += 1
        else:
            m1 += cnt // k
            cnt = 0
    m1 += cnt // k
    return m1 >= m

print(bouquets_possible_or_not([1,10,3,10,2], 3, 1, 2))
print(bouquets_possible_or_not([1,10,3,10,2], 3, 1, 3))

class Solution:
    def minDays_brute(self, bloomDay:List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if ((m*k) > n):
            return -1
        maxi = max(bloomDay)
        mini = min(bloomDay)
        for i in range(mini, maxi+1):
            if (bouquets_possible_or_not(bloomDay, m, k, i) == True):
                return i
        return -1

    def minDays_optimal(self, bloomDay:List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if ((m*k) > n):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while (low <= high):
            mid = (low + high) // 2
            if (bouquets_possible_or_not(bloomDay, m, k, mid) == True):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution().minDays_brute([1,10,3,10,2], 3,1))
print(Solution().minDays_brute([1,10,3,10,2],3,2))
print(Solution().minDays_optimal([1,10,3,10,2], 3,1))
print(Solution().minDays_optimal([1,10,3,10,2],3,2))



