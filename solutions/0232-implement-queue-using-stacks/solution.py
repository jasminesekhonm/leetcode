class MyQueue:

    def __init__(self):
        self.list = []
        

    def push(self, x: int) -> None:
        self.list.append(x)
        

    def pop(self) -> int:
        val = self.list[0]
        self.list = self.list[1:]
        return val
        

    def peek(self) -> int:
        return self.list[0]
        

    def empty(self) -> bool:
        return (len(self.list) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
