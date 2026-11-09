class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_ = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_: self.min_.append(val)
        else: self.min_.append(min(val, self.min_[-1]))

    def pop(self) -> None:
        i = self.stack.pop()
        self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]
        
