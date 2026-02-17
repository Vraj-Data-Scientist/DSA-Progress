class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []
        for i in range(0, n):
            while (st and k>0 and (st[-1] > num[i])):
                st.pop()
                k -= 1
            st.append(num[i])
        while (k > 0):
            st.pop()
            k -= 1
        if (not st):
            return '0'
        res = ''
        while (st):
            res = res + st[-1]
            st.pop()
        while (res and res[-1] == '0'):
            res = res[:-1]
        res = res[::-1]
        if (not res):
            return '0'
        return res

print(Solution().removeKdigits("1432219",3))
