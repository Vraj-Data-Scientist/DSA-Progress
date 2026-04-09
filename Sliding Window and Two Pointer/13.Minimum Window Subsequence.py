class Solution:
    def is_subsequence_brute(self, s1, s2, n1, n2):
        if n2 == 0:
            return True
        if n1 == 0:
            return False
        if (s2[n2-1] == s1[n1-1]):
            return self.is_subsequence_brute(s1, s2, n1-1, n2-1)
        return self.is_subsequence_brute(s1, s2, n1-1, n2)

    def is_subsequence(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        i, j = 0, 0
        while (i < n1 and j < n2):
            if (s2[j] == s1[i]):
                j += 1
            i += 1
        return j == n2

    def minWindow(self, s1, s2):
        n = len(s1)
        m = len(s2)
        s_index = -1
        ans = ''
        min_len = float('inf')
        for i in range(0, n):
            for j in range(i, n):
                if (self.is_subsequence(s1[i:j+1], s2)):
                    if (min_len > j-i+1):
                        min_len = j-i+1
                        ans = s1[i:j+1]
                    break
        return ans

    def minWindow_optimal(self, s1, s2):
        if not s2 or not s1:
            return ''
        min_len = float('inf')
        ans = ''
        i = 0
        n = len(s1)
        m = len(s2)
        while (i < n):
            j = i
            k = 0
            while (j < n and k < m):
                if (s1[j] == s2[k]):
                    k += 1
                j += 1
            if (k == m):
                right = j - 1
                k = m - 1
                while (right >= i and k >= 0):
                    if s1[right] == s2[k]:
                        k -= 1
                    right -= 1
                start = right + 1
                length = j - start
                if (length < min_len):
                    min_len = length
                    ans = s1[start:j]
                i = start + 1
            else:
                break
        return ans

print(Solution().is_subsequence("geeksforgeeks", 'eksrg'))
print(Solution().is_subsequence("geeksforgeeks", 'eksrgkk'))
print(Solution().is_subsequence_brute("geeksforgeeks", 'eksrg', 13, 5))
print(Solution().is_subsequence_brute("geeksforgeeks", 'eksrgkk', 13, 7))
print(Solution().minWindow("geeksforgeeks", 'eksrg'))
print(Solution().minWindow_optimal("geeksforgeeks", 'eksrg'))