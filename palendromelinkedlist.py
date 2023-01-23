class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        l, r = 0, len(stack)-1

        while l < r :

            if stack[l] != stack[r]:
                return False
                
            l += 1
            r -= 1
           
        return True