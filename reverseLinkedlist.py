# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        current = head
        new_pointer = None

        while current:
            newNode = current.next
            current.next = new_pointer
            new_pointer = current
            current = newNode

        return new_pointer