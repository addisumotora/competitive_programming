# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        stack = []
        current = head

        while current:

            stack.append(current.val)
            current = current.next
        
        stack.pop(-n)

        head = ListNode()
        current = head

        for i in range(len(stack)):
            newNode = ListNode(stack[i])
            current.next = newNode
            current = newNode
        
        return head.next