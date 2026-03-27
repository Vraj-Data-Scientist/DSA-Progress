class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [(0, chr(i)) for i in range(0, 256)]
        for char in s:
            index = ord(char)
            freq[index] = (freq[index][0] + 1, char)
        freq.sort(key=lambda x:(-x[0], x[1]))
        result = [f*ch for f,ch in freq if f > 0]
        return ''.join(result)

    def frequencySort_2(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        sorted_list = sorted(freq.items(), key=lambda x:(-x[1], x[0]))
        result = [ch * f for ch,f in sorted_list if f>0]
        return ''.join(result)

print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("Aabb"))
print(Solution().frequencySort_2("tree"))
print(Solution().frequencySort_2("cccaaa"))
print(Solution().frequencySort_2("Aabb"))
