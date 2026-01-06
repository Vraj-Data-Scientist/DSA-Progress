from typing import List
from math import ceil

def req_time(piles:List[int], k:int) -> int:
    n = len(piles)
    time = 0
    for i in range(0, n):
        time += ceil(piles[i] / k)
    return time

class Solution:
    def minEatingSpeed_brute(self, piles: List[int], h: int) -> int:
        for i in range(1, max(piles) + 1):
            if (req_time(piles, i) <= h):
                return i
        return -1

    def minEatingSpeed_optimal(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 1
        while (low <= high):
            mid = (low + high) // 2
            if (req_time(piles, mid) <= h):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


print(Solution().minEatingSpeed_brute([3,6,7,11], 8))
print(Solution().minEatingSpeed_brute([30,11,23,4,20], 5))
print(Solution().minEatingSpeed_brute([30,11,23,4,20], 6))
print(Solution().minEatingSpeed_optimal([3,6,7,11], 8))
print(Solution().minEatingSpeed_optimal([30,11,23,4,20], 5))
print(Solution().minEatingSpeed_optimal([30,11,23,4,20], 6))