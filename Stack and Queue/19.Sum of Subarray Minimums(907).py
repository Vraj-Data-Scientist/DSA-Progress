from typing import List

class Solution:
    def sumSubarrayMins_brute(self, arr: List[int]) -> int:
        n = len(arr)
        sum = 0
        mod = 10**9 + 7
        for i in range(0, n):
            mini = arr[i]
            for j in range(i, n):
                mini = min(mini, arr[j])
                sum = (sum + mini) % mod
        return sum

    def nse(self, arr: List[int]):
        n = len(arr)
        st = []
        nse = [-1] * n
        for i in range(n-1, -1, -1):
            while (st and arr[st[-1]] >= arr[i]):
                st.pop()
            nse[i] =n if not st else st[-1]
            st.append(i)
        return nse

    def psee(self, arr: List[int]):
        n = len(arr)
        st = []
        psee = [-1] * n
        for i in range(0, n):
            while (st and arr[st[-1]] > arr[i]):
                st.pop()
            psee[i] = -1 if not st else st[-1]
            st.append(i)
        return psee

    def sumSubarrayMins_optimal(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7
        nse = self.nse(arr)
        psee = self.psee(arr)
        sum = 0
        for i in range(0, n):
            right = nse[i] - i
            left = i - psee[i]
            sum = (sum + ((right * left * 1 * arr[i]) % mod)) % mod
        return sum

print(Solution().sumSubarrayMins_brute([3,1,2,4]))
print(Solution().sumSubarrayMins_brute([11,81,94,43,3]))
print(Solution().sumSubarrayMins_optimal([3,1,2,4]))
print(Solution().sumSubarrayMins_optimal([11,81,94,43,3]))
