from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        size = len(self.q)
        self.q.append(x)
        for i in range(0, size):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

st = MyStack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.top())
print(st.pop())
print(st.top())
print(st.empty())
