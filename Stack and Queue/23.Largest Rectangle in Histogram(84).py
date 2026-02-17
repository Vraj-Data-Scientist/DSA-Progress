from typing import List

def nse_i(a):
    n = len(a)
    nse = [-1]*n
    st = []
    for i in range(n-1, -1, -1):
        while (st and a[st[-1]] >= a[i]):
            st.pop()
        nse[i] = st[-1] if st else n
        st.append(i)
    return nse

def pse_i(a):
    n = len(a)
    pse = [-1]*n
    st = []
    for i in range(0, n):
        while (st and a[st[-1]] >= a[i]):
            st.pop()
        pse[i] = st[-1] if st else -1
        st.append(i)
    return pse

class Solution:
    def largestRectangleArea_brute(self, heights: List[int]) -> int:
        n = len(heights)
        nse = nse_i(heights)
        pse = pse_i(heights)
        maxi = 0
        for i in range(0, n):
            area = heights[i] * (nse[i] - pse[i] - 1)
            maxi = max(maxi, area)
        return maxi

    def largestRectangleArea_optimal(self, heights: List[int]) -> int:
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


print(Solution().largestRectangleArea_brute([2,1,5,6,2,3]))
print(Solution().largestRectangleArea_brute([2,4]))
print(Solution().largestRectangleArea_optimal([2,1,5,6,2,3]))
print(Solution().largestRectangleArea_optimal([2,4]))