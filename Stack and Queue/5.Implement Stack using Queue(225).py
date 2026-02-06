class queue:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0]*self.capacity
        self.start = -1
        self.end = -1
        self.curr_size = 0
    def enqueue(self, x):
        if (self.curr_size == self.capacity):
            print('full')
            return
        if (self.curr_size == 0):
            self.start = self.end = 0
        else:
            self.end = (self.end + 1) % self.capacity
        self.arr[self.end] = x
        self.curr_size += 1
    def dequeue(self):
        if (self.curr_size == 0):
            print('empty')
        ele = self.arr[self.start]
        if (self.curr_size == 1):
            self.start = self.end = -1
        else:
            self.start = (self.start + 1) % self.capacity
        self.curr_size -= 1
        return ele
    def get_front(self):
        if (self.curr_size == 0):
            print('empty')
        return self.arr[self.start]
    def get_rear(self):
        if (self.curr_size == 0):
            print('empty')
        return self.arr[self.end]
    def get_size(self):
        return self.curr_size
class stack:
    def __init__(self):
        self.q = queue(5)
    def push(self, x):
        size = self.q.get_size()
        self.q.enqueue(x)
        for i in range(0, size):
            self.q.enqueue(self.q.get_front())
            self.q.dequeue()
    def pop(self):
        return self.q.dequeue()
    def peek(self):
        return self.q.get_front()
    def size(self):
        return self.q.get_size()

st = stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.peek())
print(st.pop())
print(st.peek())
print(st.size())
