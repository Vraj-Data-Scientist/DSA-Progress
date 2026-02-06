class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = []
        for i in range(0, n):
            if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
                st.append(s[i])
            else:
                if (not st):
                    return False
                if ((s[i] == ')' and st[-1] == '(') or (s[i] == '}' and st[-1] == '{') or (s[i] == ']' and st[-1] == '[')):
                    st.pop()
                else:
                    return False
        return len(st) == 0

print(Solution().isValid('()[{}()]'))
print(Solution().isValid('()[{}(])'))