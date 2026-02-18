from typing import List

class StockSpanner_brute:
    def __init__(self):
        self.list1 = []

    def next(self, price: int) -> int:
        self.list1.append(price)
        n = len(self.list1)
        cnt = 1
        for i in range(n-2, -1, -1):
            if (self.list1[i] <= price):
                cnt += 1
            else:
                break
        return cnt

class StockSpanner:
    def __init__(self):
        self.st = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        while (self.st and self.st[-1][0] <= price):
            self.st.pop()
        ans = self.index - (self.st[-1][1] if self.st else -1)
        self.st.append([price, self.index])
        return ans

spb = StockSpanner_brute()
print(spb.next(100))
print(spb.next(80))
print(spb.next(60))
print(spb.next(70))
print(spb.next(60))
print(spb.next(75))
print(spb.next(85))
sp = StockSpanner()
print(sp.next(100))
print(sp.next(80))
print(sp.next(60))
print(sp.next(70))
print(sp.next(60))
print(sp.next(75))
print(sp.next(85))


