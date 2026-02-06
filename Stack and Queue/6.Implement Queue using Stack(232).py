class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        
    def push(self, x: int) -> None:
        self.input.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self) -> bool:
        return not self.input and not self.output

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.push(5))
print(q.pop())
print(q.peek())
q.push(5)
print(q.peek())
