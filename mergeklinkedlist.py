# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        stack = []

        for head in lists:
            current = head
            while current:
                stack.append(current.val)
                current = current.next
        
        stack = sorted(stack)

        head = ListNode()
        current = head

        for i in stack:
            newNode = ListNode(i)
            current.next = newNode
            current = newNode
        
        return head.next