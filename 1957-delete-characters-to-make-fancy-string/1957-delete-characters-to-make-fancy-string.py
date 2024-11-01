class Solution:
    def makeFancyString(self, s: str) -> str:
        
        output = ''
        count = 0
        
        for item in s:
            if output and output[-1] == item and count == 2:
                continue
            
            else:
                if output and  item == output[-1]:
                    output += item
                    count += 1
                else:
                    output += item
                    count = 1
                
        return output
        