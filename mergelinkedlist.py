# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = []
        l1 = list1
        l2 = list2

        while l1:
            ans.append(l1.val)
            l1 = l1.next
        
        while l2:
            ans.append(l2.val)
            l2 = l2.next

        ans = sorted(ans)

        head = ListNode()
        current = head

        for i in ans:
            newnode = ListNode(i)
            current.next = newnode
            current = newnode
        
        return head.next
