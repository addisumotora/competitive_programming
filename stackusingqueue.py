class MyStack:

    def __init__(self):
        self.mystack = []

    def push(self, x: int) -> None:
        self.mystack.append(x)

    def pop(self) -> int:
        return self.mystack.pop()

    def top(self) -> int:
        return self.mystack[-1]

    def empty(self) -> bool:
        if len(self.mystack)==0:
            return True
        return False