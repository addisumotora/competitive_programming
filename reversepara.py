class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        i=0
        while(i<len(s)):
            if s[i]!=')':
                stack.append(s[i])
            else:
                newstack = []
                while stack[-1] and stack[-1]!='(':
                    newstack.append(stack.pop())
                stack.pop()
                stack.extend(newstack)
            i+=1
        return "".join(stack)