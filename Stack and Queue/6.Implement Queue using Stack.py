class stack:
    def __init__(self, cap):
        self.capacity = cap
        self.top = -1
        self.arr = [0] * self.capacity
    def push(self, x):
        if (self.top == self.capacity - 1):
            print('overflow')
            return
        self.top += 1
        self.arr[self.top] = x
    def pop(self):
        if (self.top == -1):
            print('underflow')
            return
        ele = self.arr[self.top]
        self.top -= 1
        return ele
    def peek(self):
        if (self.top == -1):
            print('empty')
            return
        return self.arr[self.top]
    def size(self):
        return self.top + 1

class queue:
    def __init__(self):
        self.s1 = stack(5)
        self.s2 = stack(5)
    def enqueue(self, x):
        self.s1.push(x)
    def dequeue(self):
        if (self.s2.size() > 0):
            return self.s2.pop()
        else:
            while (self.s1.size()):
                self.s2.push(self.s1.peek())
                self.s1.pop()
            return self.s2.pop()
    def get_front(self):
        if (self.s2.size() > 0):
            return self.s2.peek()
        else:
            while (self.s1.size()):
                self.s2.push(self.s1.peek())
                self.s1.pop()
            return self.s2.peek()

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.enqueue(5))
print(q.dequeue())
print(q.get_front())
q.enqueue(5)
print(q.get_front())