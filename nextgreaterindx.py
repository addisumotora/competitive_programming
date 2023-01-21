class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        output = []
        i = 0

        while head:
            vl = head.val
            output.append(0)

            while stack and stack[-1][0] < vl:
                indx = stack.pop()[1]
                output[indx] = vl
            
            stack.append((vl,i))
            i += 1
            head = head.next
            
        return output