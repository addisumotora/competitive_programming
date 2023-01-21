class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next
        
        stack = sorted(stack)

        head = ListNode()
        current = head
        for i in stack:
            node = ListNode(i)
            current.next = node
            current = node

        return head.next