from typing import List

class Solution:
    def maxProfit_brute(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(0, n):
            for j in range(i, n):
                if (prices[j] - prices[i] > max_profit):
                    max_profit = prices[j] - prices[i]
        return max_profit if max_profit>0 else 0

    def maxProfit_optimal(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        mini = prices[0]
        for i in range(0, n):
            cost = prices[i] - mini
            max_profit = max(max_profit, cost)
            mini = min(mini, prices[i])
        return max_profit if max_profit>0 else 0

print(Solution().maxProfit_brute([7,1,5,3,6,4]))
print(Solution().maxProfit_brute([7,6,4,3,1]))
print(Solution().maxProfit_optimal([7,1,5,3,6,4]))
print(Solution().maxProfit_optimal([7,6,4,3,1]))