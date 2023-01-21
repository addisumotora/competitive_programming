class Solution:
    def deleteNode(self, node):

        current = node
        prev = current
        while current:
            if current.next == None:
                prev.next = None
                break
                
            current.val = current.next.val
            prev = current 
            current = current.next