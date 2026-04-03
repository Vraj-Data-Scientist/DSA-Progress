class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1
        for i in range(0, len(haystack)):
            if (haystack[i:i+m] == needle):
                return i
        return -1

    def compute_lps(self, needle):
        if needle == "":
            return 0
        lps = [0] * len(needle)
        length, i = 0, 1
        # length = shows length of (longest prefix) that is also a suffix for current substring(to track new character after length)
        # lps[i] = shows length of longest prefix that is also a suffix for current substring(useful for algo)
        while (i < len(needle)):
            # ((len+1)th/new character and current character) matched means increase the length
            if (needle[i] == needle[length]):
                length += 1
                lps[i] = length
                i += 1
            # not matched and if length is 0 already then lps[i] = 0
            elif (length == 0):
                lps[i] = 0
                i += 1
            # not matched and if length is not 0 means we need to decrease the length
            # length - 1 means last matched character index of (longest prefix) for which suffix is there in substring
            # It jumps to length = lps[length - 1] instead of length = 0
            else:
                length = lps[length-1]
        return lps

    def kmp(self, haystack, needle):
        i = 0
        j = 0
        lps = self.compute_lps(needle)
        result = []
        while i < len(haystack):
            if (haystack[i] == needle[j]):
                i, j = i+1, j+1
                if (j == len(needle)):
                    result.append(i - len(needle))
                    j = lps[j-1]
            else:
                if j == 0:
                    i += 1
                else:
                    # j-1 is last matched character...we find lps[j-1](string[0:j]) and start with that instead of start with j==0
                    j = lps[j-1]
        return result

    def rabin_karp(self, source, target):
        base = 10**6
        target_hash = 0
        result = []
        n = len(source)
        m = len(target)
        for char in target:
            target_hash = ((target_hash * 31) + ord(char)) % base
        source_hash = 0
        power = 1
        for i in range(0, m):
            power = power * 31
        for i in range(0, len(source)):
            source_hash = ((source_hash * 31) + ord(source[i])) % base
            if i < m-1:
                continue
            if i >= m:
                source_hash = (source_hash - (ord(source[i-m])*power)) % base
            if source_hash < 0:
                source_hash += base
            if source_hash == target_hash:
                if (source[i-m+1:i+1] == target):
                    result.append(i-m+1)
        return result



print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("leetcode", "leeto"))
print(Solution().kmp("sadbutsad", "sad"))
print(Solution().kmp("leetcode", "leeto"))
print(Solution().rabin_karp("sadbutsad", "sad"))
