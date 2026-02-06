class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if (not self.st):
            self.st.append((val, val))
        else:
            self.st.append((val, min(val, self.st[-1][1])))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]

st = MinStack()
st.push(-2)
st.push(0)
st.push(-3)
print(st.getMin())
st.pop()
print(st.top())
print(st.getMin())




class MinStack_optimal:

    def __init__(self):
        self.st = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if (val > self.mini):
            self.st.append(val)
        else:
            self.st.append(2*val - self.mini)
            self.mini = val

    def pop(self) -> None:
        if (not self.st):
            return
        x = self.st[-1]
        self.st.pop()
        if (x < self.mini):
            self.mini = 2*self.mini - x

    def top(self) -> int:
        if (not self.st):
            return
        x  = self.st[-1]
        if (x < self.mini):
            return self.mini
        else:
            return x

    def getMin(self) -> int:
        return self.mini

st = MinStack_optimal()
st.push(-2)
st.push(0)
st.push(-3)
print(st.getMin())
st.pop()
print(st.top())
print(st.getMin())