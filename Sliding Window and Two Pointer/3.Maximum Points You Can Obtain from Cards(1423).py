class Solution(object):
    def maxScore_optimal(self, cardPoints, k):
        l_sum = 0
        for i in range(0, k):
            l_sum += cardPoints[i]
        max_point = l_sum
        n = len(cardPoints)
        r_index = n - 1
        r_sum = 0
        for j in range(k - 1, -1, -1):
            l_sum -= cardPoints[j]
            r_sum += cardPoints[r_index]
            r_index -= 1
            max_point = max(max_point, l_sum + r_sum)
        return max_point

print(Solution().maxScore_optimal([9,7,7,9,7,7,9],7))