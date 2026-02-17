from typing import List

def nse(a):
    n = len(a)
    nse = [-1]*n
    st = []
    for i in range(n-1, -1, -1):
        while (st and a[st[-1]] >= a[i]):
            st.pop()
        nse[i] = st[-1] if st else n
        st.append(i)
    return nse

def psee(a):
    n = len(a)
    psee = [-1]*n
    st = []
    for i in range(0, n):
        while (st and a[st[-1]] > a[i]):
            st.pop()
        psee[i] = st[-1] if st else -1
        st.append(i)
    return psee

def nge(a):
    n = len(a)
    nge = [-1]*n
    st = []
    for i in range(n-1, -1, -1):
        while (st and a[st[-1]] <= a[i]):
            st.pop()
        nge[i] = st[-1] if st else n
        st.append(i)
    return nge

def pgee(a):
    n = len(a)
    pgee = [-1]*n
    st = []
    for i in range(0, n):
        while (st and a[st[-1]] < a[i]):
            st.pop()
        pgee[i] = st[-1] if st else -1
        st.append(i)
    return pgee

def sum_subarray_min(a):
    n = len(a)
    nse_list = nse(a)
    psee_list = psee(a)
    sum = 0
    for i in range(0, n):
        right = nse_list[i] - i
        left = i - psee_list[i]
        sum = sum + (right * left * a[i])
    return sum

def sum_subarray_max(a):
    n = len(a)
    nge_list = nge(a)
    pgee_list = pgee(a)
    sum = 0
    for i in range(0, n):
        right = nge_list[i] - i
        left = i - pgee_list[i]
        sum = sum + (right * left * a[i])
    return sum

class Solution:
    def subArrayRanges_brute(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for i in range(0, n):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i+1, n):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                sum = sum + (maxi - mini)
        return sum

    def subArrayRanges(self, nums: List[int]) -> int:
        return sum_subarray_max(nums) - sum_subarray_min(nums)

print(Solution().subArrayRanges([1,4,3,2]))
print(Solution().subArrayRanges([1,2,3]))
print(Solution().subArrayRanges([1,3,3]))
print(Solution().subArrayRanges([4,-2,-3,4,1]))
print(Solution().subArrayRanges_brute([1,4,3,2]))
print(Solution().subArrayRanges_brute([1,2,3]))
print(Solution().subArrayRanges_brute([1,3,3]))
print(Solution().subArrayRanges_brute([4,-2,-3,4,1]))
