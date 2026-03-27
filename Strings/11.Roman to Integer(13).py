class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = dict1[s[0]]
        for i in range(1, len(s)):
            if (dict1[s[i]] <= dict1[s[i-1]]):
                result += dict1[s[i]]
            else:
                result += dict1[s[i]]
                result -= (2*dict1[s[i-1]])
        return result

    def romanToInt_2(self, s: str) -> int:
        dict1 = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = 0
        for a,b in zip(s, s[1:]):
            if (dict1[a] >= dict1[b]):
                result += dict1[a]
            else:
                result -= dict1[a]
        return result + dict1[s[-1]]

print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt_2("III"))
print(Solution().romanToInt_2("LVIII"))
print(Solution().romanToInt_2("MCMXCIV"))