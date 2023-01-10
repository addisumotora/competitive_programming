# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        string1 = ""
        string2 = ""
        list1 = l1
        list2 = l2

        while list1:
            string1 += str(list1.val)
            list1 = list1.next

        while list2:
            string2 += str(list2.val)
            list2 = list2.next
        
        s = list(str(int(string1[::-1]) + int(string2[::-1])))


        head = ListNode(int(s[-1]))
        current = head

        for i in range(len(s)-2,-1,-1):
            newnode = ListNode(int(s[i]))
            current.next = newnode
            current = newnode
        
        return head
