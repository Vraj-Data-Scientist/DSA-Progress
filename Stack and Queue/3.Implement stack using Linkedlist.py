class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, x):
        temp = ListNode(x)
        temp.next = self.top
        self.top = temp
        self.size += 1
    def pop(self):
        if (self.top == None):
            print('stack underflow')
            return
        temp = self.top
        self.top = self.top.next
        ele = temp
        temp = None
        self.size = self.size - 1
        return ele
    def peek(self):
        if (self.top == None):
            print('stack empty')
            return -1
        return self.top.val
    def size_stack(self):
        return self.size

st = stack()
print(st.peek())
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.peek())
st.pop()
st.pop()
print(st.peek())
print(st.size_stack())


