from typing import List

def given_dist_possible(stalls:List[int], cows:int, dist:int):
    cnt_cows = 1
    last = stalls[0]
    n = len(stalls)
    for i in range(1, n):
        if (stalls[i] - last >= dist):
            cnt_cows += 1
            last = stalls[i]
        if (cnt_cows >= cows):
            return True
    return False

print(given_dist_possible([1,2,3,4,6], 2, 5))

class Solution:
    def aggressiveCows_brute(self, stalls:List[int], cows:int):
        stalls.sort()
        for i in range(1, max(stalls)-min(stalls)+2):
            if (given_dist_possible(stalls, cows, i) == True):
                continue
            else:
                return (i-1)
        return -1

    def aggressiveCows_optimal(self, stalls:List[int], cows:int):
        stalls.sort()
        n = len(stalls)
        low = 1
        high = stalls[n-1] - stalls[0]
        while (low <= high):
            mid = (low+high) // 2
            if (given_dist_possible(stalls, cows, mid) == True):
                low = mid + 1
            else:
                high = mid - 1
        return high


print(Solution().aggressiveCows_brute([0,3,4,7,10,9], 4))
print(Solution().aggressiveCows_brute([4,2,1,3,6], 2))
print(Solution().aggressiveCows_optimal([0,3,4,7,10,9], 4))
print(Solution().aggressiveCows_optimal([4,2,1,3,6], 2))