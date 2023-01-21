class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

                dummyhead = ListNode(0,head)
        prev,curr = head, head.next

        while curr:

            if curr.val >= prev.val:
                prev, curr = curr, curr.next
                continue
            
            temp = dummyhead

            while curr.val > temp.next.val:
                temp = temp.next

            prev.next = curr.next
            curr.next = temp.next
            temp.next = curr
            curr = prev.next

        return dummyhead.next



# /////////////////////////////


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