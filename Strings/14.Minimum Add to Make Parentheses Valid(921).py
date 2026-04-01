class Solution:
    def minAddToMakeValid_brute(self, s: str) -> int:
        st = []
        cnt = 0
        for ch in s:
            if (ch == '('):
                st.append(ch)
            elif (st and ch == ')'):
                st.pop()
            elif (not st and ch == ')'):
                cnt += 1
        if (st):
            cnt += len(st)
        return cnt

    def minAddToMakeValid_better(self, s: str) -> int:
        st = []
        opening_c = 0
        closing_c = 0
        for ch in s:
            if (ch == '('):
                opening_c += 1
            elif (ch == ')' and opening_c > 0):
                opening_c -= 1
            elif (ch == ')' and opening_c == 0):
                closing_c += 1
        return opening_c + closing_c

print(Solution().minAddToMakeValid_brute("(()))("))
print(Solution().minAddToMakeValid_better("(()))("))