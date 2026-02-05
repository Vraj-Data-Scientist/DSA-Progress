class stack:
    def __init__(self, cap):
        self.capacity = cap
        self.top = -1
        self.arr = [0] * self.capacity
    def push(self, x):
        if (self.top == self.capacity - 1):
            print('stack overflow')
            return
        self.top += 1
        self.arr[self.top] = x
    def pop(self):
        if (self.top == -1):
            print('stack underflow')
            return
        ele = self.arr[self.top]
        self.top -= 1
        return ele
    def peek(self):
        if (self.top == -1):
            print('stack empty')
            return
        return self.arr[self.top]
    def size(self):
        return self.top + 1

st = stack(10)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.peek())
print(st.pop())
print(st.peek())
print(st.size())
