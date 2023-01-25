class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        stack = []
        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        l,r = 0, len(stack)-1
        temp = 0

        while l < r:
            summ = stack[l] + stack[r]
            temp = max(temp,summ)

            l += 1
            r -= 1
        
        return temp
        