class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        stack = sorted(stack)

        head = ListNode(0)
        cur = head

        for i in stack:
            node = ListNode(i)
            cur.next = node
            cur = node
        
        return head.next