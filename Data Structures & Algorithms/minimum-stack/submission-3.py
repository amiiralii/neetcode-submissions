class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum.append( min(self.getMin(), val) )
        
    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minimum = self.minimum[:-1]
        
    def top(self) -> int:
        top = self.stack[-1]
        return top
        
    def getMin(self) -> int:
        if len(self.minimum) == 0:
            return math.inf
        return self.minimum[-1]
        