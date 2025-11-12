class Solution(object):
    def totalFruit_brute(self, fruits):
        n = len(fruits)
        max_len = 0
        for i in range(0, n):
            set1 = set()
            for j in range(i,n):
                set1.add(fruits[j])
                if (len(set1) > 2):
                    break
                if (len(set1) <= 2):
                    max_len = max(max_len, j-i+1)
        return max_len

    def totalFruit_better(self, fruits):
        n = len(fruits)
        dict1 = {}
        l = 0
        r = 0
        max_len = 0
        while (r < n):
            dict1[fruits[r]] = dict1.get(fruits[r], 0) + 1
            while (len(dict1) > 2):
                dict1[fruits[l]] -= 1
                if (dict1[fruits[l]] == 0):
                    del dict1[fruits[l]]
                l += 1
            if (len(dict1) <= 2):
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len

    def totalFruit_optimal(self, fruits):
        n = len(fruits)
        dict1 = {}
        l = 0
        r = 0
        max_len = 0
        while (r < n):
            dict1[fruits[r]] = dict1.get(fruits[r], 0) + 1
            if (len(dict1) > 2):
                dict1[fruits[l]] -= 1
                if (dict1[fruits[l]] == 0):
                    del dict1[fruits[l]]
                l += 1
            if (len(dict1) <= 2):
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len

print(Solution().totalFruit_brute([1,2,3,2,2]))
print(Solution().totalFruit_better([1,2,3,2,2]))
print(Solution().totalFruit_optimal([1,2,3,2,2]))