class MyLinkedList:

    def __init__(self):
        self.queue = []

    def get(self, index: int) -> int:
        n = len(self.queue)

        if index > n - 1:
            return -1

        return self.queue[index]

    def addAtHead(self, val: int) -> None:
         self.queue.insert(0,val)

    def addAtTail(self, val: int) -> None:
        self.queue.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == len(self.queue):
            self.queue.append(val)
        elif index < len(self.queue):
            self.queue.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.queue):
            self.queue.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)