class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_ = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_ or self.min_[-1]>=val:
            self.min_.append(val)

    def pop(self) -> None:
        i = self.stack.pop()
        if self.min_[-1]==i: self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]
        
