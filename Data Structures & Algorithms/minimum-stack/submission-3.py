class MinStack:

    def __init__(self):
        self.stack = [] # (val, min_val)

    def push(self, val: int) -> None:
        new_min = min(self.stack[-1][1] if self.stack else val, val)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
