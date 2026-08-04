from collections import deque
class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = deque([])
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minVal) == 0:
            self.minVal.append(val)
        
        elif val<=self.minVal[-1]:
            self.minVal.append(val) 

    def pop(self) -> None:
        if self.stack[-1] == self.minVal[-1]:
            self.minVal.pop()
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
        
