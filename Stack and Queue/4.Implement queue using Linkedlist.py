class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.curr_size = 0
    def enqueue(self, x):
        temp = ListNode(x)
        if (self.curr_size == 0):
            self.start = self.end = temp
        else:
            self.end.next = temp
            self.end = temp
        self.curr_size += 1
    def dequeue(self):
        if (self.curr_size == 0):
            print('queue empty')
        ele = self.start.val
        if (self.curr_size == 1):
            self.start = self.end = None
        else:
            self.start = self.start.next
        self.curr_size -= 1
        return ele
    def get_front(self):
        if (self.curr_size == 0):
            print('queue empty')
        return self.start.val
    def get_rear(self):
        if (self.curr_size == 0):
            print('queue empty')
        return self.end.val
    def get_size(self):
        return self.curr_size

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.get_size())
print(q.get_front())
print(q.get_rear())
q.enqueue(5)
print(q.get_rear())
print(q.get_front())