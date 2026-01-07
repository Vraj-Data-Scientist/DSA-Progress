from typing import List

def req_days(nums:List[int], capacity:int) -> int:
    n = len(nums)
    sum = 0
    days_req = 1
    for i in range(0, n):
        sum += nums[i]
        if (sum <= capacity):
            continue
        else:
            days_req += 1
            sum = nums[i]
    return days_req

print(req_days([10,50,100,100,50,100,100,100], 159))
print(req_days([10,50,100,100,50,100,100,100], 160))

class Solution:
    def shipWithinDays_brute(self, weights: List[int], days: int) -> int:
        n = len(weights)
        mini = max(weights)
        maxi = sum(weights)
        # print(maxi)
        for i in range(mini, maxi+1):
            if (req_days(weights, i) <= days):
                return i
        return -1

    def shipWithinDays_optimal(self, weights: List[int], days: int) -> int:
        n = len(weights)
        mini = max(weights)
        maxi = sum(weights)
        low = mini
        high = maxi
        while (low <= high):
            mid = (low + high) // 2
            if (req_days(weights, mid) <= days):
                high = mid - 1
            else:
                low = mid + 1
        return low

print(Solution().shipWithinDays_brute([1,2,3,4,5,6,7,8,9,10], 5))
print(Solution().shipWithinDays_brute([3,2,2,4,1,4], 3))
print(Solution().shipWithinDays_brute([1,2,3,1,1], 4))
print(Solution().shipWithinDays_optimal([1,2,3,4,5,6,7,8,9,10], 5))
print(Solution().shipWithinDays_optimal([3,2,2,4,1,4], 3))
print(Solution().shipWithinDays_optimal([1,2,3,1,1], 4))

