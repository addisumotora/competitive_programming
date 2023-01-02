class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        di={}
        stack=[]
        for i in range(len(s)):
            di[s[i]] = i
        
        temp = 0

        for i in range(len(s)):
            if temp<di[s[i]]:
                temp = di[s[i]]
            if stack and temp==i:
                
                summ=0
                for j in stack:
                    summ +=j
                stack.append((i+1)-summ)

            elif temp==i:
                stack.append(i+1)
        
        return stack