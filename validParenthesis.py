class Solution:
    def isValid(self, s: str) -> bool:
        parathesis = {'(':')','{':'}','[':']'}
        stack =[]
        count = 0
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            else:
                if stack[-1] in parathesis and parathesis[stack[-1]]==s[i]:
                    stack.pop(-1)
                    count = count+1
                else:
                    stack.append(s[i])
        if len(stack)==0:
            return True
        return False