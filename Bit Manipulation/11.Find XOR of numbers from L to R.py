class Solution:
    def xor_brute(self, n):
        xor = 0
        for i in range(1, n+1):
            xor = xor ^ i
        return xor

    def xor(self, n):
        if (n % 4 == 1): return 1
        elif (n % 4 == 2): return n+1
        elif (n % 4 == 3): return 0
        else: return n

    def getXor(self, a, b):
        return self.xor(a-1) ^ self.xor(b)

print(Solution().getXor(4, 8))