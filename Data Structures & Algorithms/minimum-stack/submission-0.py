class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if self.stack:
            currentmin=self.stack[-1][1]
            newmin=min(currentmin,val)
            self.stack.append((val,newmin))
        else:
            self.stack.append((val,val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
