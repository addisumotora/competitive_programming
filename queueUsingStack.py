class MyQueue:

    def __init__(self):
        self.MyQueue = []
    
    def push(self, x: int) -> None:
        self.MyQueue.append(x)

    def pop(self) -> int:
        return self.MyQueue.pop(0)

    def peek(self) -> int:
        return self.MyQueue[0]

    def empty(self) -> bool:
        if len(self.MyQueue)>0:
            return False
        else:
            return True