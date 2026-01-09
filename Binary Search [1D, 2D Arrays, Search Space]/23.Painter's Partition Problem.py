from typing import List

def count_painters(boards:List[int], max_time:int):
    n = len(boards)
    painters = 1
    boards_painter = 0
    for i in range(0, n):
        if (boards_painter + boards[i] <= max_time):
            boards_painter += boards[i]
        else:
            painters += 1
            boards_painter = boards[i]
    return painters

class Solution:
    def find_largest_min_brute(self, boards: List[int], k: int) -> int:
        n = len(boards)
        if (k > n):
            return -1
        low = max(boards)
        high = sum(boards)
        for i in range(low, high+1):
            if (count_painters(boards, i) == k):
                return i
        return low

    def find_largest_min_optimal(self, boards: List[int], k: int) -> int:
        n = len(boards)
        if (k > n):
            return -1
        low = max(boards)
        high = sum(boards)
        while(low <= high):
            mid = (low+high) // 2
            if (count_painters(boards, mid) > k):
                low = mid + 1
            else:
                high = mid - 1
        return low

print(Solution().find_largest_min_brute([5, 5, 5, 5], 2))
print(Solution().find_largest_min_brute([10, 20, 30, 40], 2))
print(Solution().find_largest_min_optimal([5, 5, 5, 5], 2))
print(Solution().find_largest_min_optimal([10, 20, 30, 40], 2))
