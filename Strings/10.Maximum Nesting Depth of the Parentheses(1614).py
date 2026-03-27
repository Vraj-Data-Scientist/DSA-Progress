class Solution:
    def maxDepth_brute(self, s: str) -> int:
        maxi = 0
        st = []
        for char in s:
            if char == '(':
                st.append(char)
            elif char == ')':
                st.pop()
            maxi = max(maxi, len(st))
        return maxi

    def maxDepth_optimal(self, s: str) -> int:
        maxi = 0
        counter = 0
        for char in s:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
            maxi = max(maxi, counter)
        return maxi

print(Solution().maxDepth_brute("()(())((()()))"))
print(Solution().maxDepth_brute("(1)+((2))+(((3)))"))
print(Solution().maxDepth_brute("(1+(2*3)+((8)/4))+1"))
print(Solution().maxDepth_optimal("()(())((()()))"))
print(Solution().maxDepth_optimal("(1)+((2))+(((3)))"))
print(Solution().maxDepth_optimal("(1+(2*3)+((8)/4))+1"))