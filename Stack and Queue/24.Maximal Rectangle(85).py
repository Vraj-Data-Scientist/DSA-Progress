from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    st = []
    maxi = 0
    for i in range(0, n):
        while (st and heights[st[-1]] > heights[i]):
            ele_index = st[-1]
            st.pop()
            pse = st[-1] if st else -1
            nse = i
            area = heights[ele_index] * (nse - pse - 1)
            maxi = max(maxi, area)
        st.append(i)
    while (st):
        ele_index = st[-1]
        st.pop()
        pse = st[-1] if st else -1
        nse = n
        area = heights[ele_index] * (nse - pse - 1)
        maxi = max(maxi, area)
    return maxi

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        p_sum = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(0, m):
            pre_sum = 0
            for i in range(0, n):
                pre_sum += int(matrix[i][j])
                if (matrix[i][j] == '0'):
                    pre_sum = 0
                p_sum[i][j] = pre_sum
        area = 0
        for i in range(0, n):
            area = max(area, largestRectangleArea(p_sum[i]))
        return area

print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(Solution().maximalRectangle([["0"]]))
print(Solution().maximalRectangle([["1"]]))
