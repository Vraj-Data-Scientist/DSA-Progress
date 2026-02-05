class queue:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0]*self.capacity
        self.start = -1
        self.end = -1
        self.curr_size = 0
    def enqueue(self, x):
        if (self.curr_size == self.capacity):
            print('queue full')
            return
        if (self.curr_size == 0):
            self.start = self.end = 0
        else:
            self.end = (self.end + 1) % self.capacity
        self.arr[self.end] = x
        self.curr_size += 1
    def dequeue(self):
        if (self.curr_size == 0):
            print('queue empty')
        ele = self.arr[self.start]
        if (self.curr_size == 1):
            self.start = self.end = -1
        else:
            self.start = (self.start + 1) % self.capacity
        self.curr_size -= 1
        return ele
    def get_front(self):
        if (self.curr_size == 0):
            print('queue empty')
        return self.arr[self.start]
    def get_rear(self):
        if (self.curr_size == 0):
            print('queue empty')
        return self.arr[self.end]
    def get_size(self):
        return self.curr_size

q = queue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.enqueue(5))
print(q.dequeue())
print(q.get_size())
print(q.get_front())
print(q.get_rear())
q.enqueue(5)
print(q.get_rear())
print(q.get_front())





