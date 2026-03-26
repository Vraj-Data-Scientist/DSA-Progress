class Solution:
    def removeOuterParentheses_brute(self, s: str) -> str:
        st = []
        res = ''
        for i in range(0, len(s)):
            if (s[i] == '('):
                if (st):
                    res += s[i]
                st.append(s[i])
            else:
                st.pop()
                if (st):
                    res += s[i]
        return res

    def removeOuterParentheses_optimal(self, s: str) -> str:
        cnt = 0
        res = ''
        for i in range(0, len(s)):
            if (s[i] == ')'):
                cnt -= 1
            if (cnt != 0):
                res += s[i]
            if (s[i] == '('):
                cnt += 1
        return res

print(Solution().removeOuterParentheses_brute("(()())(())"))
print(Solution().removeOuterParentheses_brute("(()())(())(()(()))"))
print(Solution().removeOuterParentheses_brute("()()"))
print(Solution().removeOuterParentheses_optimal("(()())(())"))
print(Solution().removeOuterParentheses_optimal("(()())(())(()(()))"))
print(Solution().removeOuterParentheses_optimal("()()"))