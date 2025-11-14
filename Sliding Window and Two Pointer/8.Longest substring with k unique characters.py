class Solution:
    def kDistinctChar_brute(self, s, k):
        n = len(s)
        max_len = 0
        for i in range(0,n):
            set1 = set()
            for j in range(i,n):
                set1.add(s[j])
                if (len(set1) == k):
                    max_len = max(max_len, j-i+1)
        return max_len

    def kDistinctChar_better(self, s, k):
        n= len(s)
        l, r = 0, 0
        dict1 = {}
        max_len = 0
        while (r < n):
            dict1[s[r]] = dict1.get(s[r], 0) + 1
            while (len(dict1) > k):
                dict1[s[l]] -= 1
                if (dict1[s[l]] == 0):
                    del dict1[s[l]]
                l += 1
            if (len(dict1) == k):
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len if max_len > 0 else -1

    def kDistinctChar_optimal(self, s, k):
        n= len(s)
        l, r = 0, 0
        dict1 = {}
        max_len = 0
        while (r < n):
            dict1[s[r]] = dict1.get(s[r], 0) + 1
            if (len(dict1) > k):
                dict1[s[l]] -= 1
                if (dict1[s[l]] == 0):
                    del dict1[s[l]]
                l += 1
            if (len(dict1) == k):
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len if max_len > 0 else -1

print(Solution().kDistinctChar_brute('aabacbebebe', 3))
print(Solution().kDistinctChar_better('aabacbebebe', 3))
print(Solution().kDistinctChar_optimal('aabacbebebe', 3))