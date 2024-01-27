class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        result = 0
        
        parity = 1
        
        i = 0

        while i < len(s) and s[i] == ' ':
            i += 1
            
        if i == len(s):
            return result
        
        if s[i] == '-':
            parity = -1
            i += 1
            
        elif s[i] == '+':
            i += 1
            
        for j in range(i, len(s)):
            
            if not s[j].isdigit():
                break       

            result = result * 10 + int(s[j])
                      
        result = result * parity
        
        if result <  MIN_INT: return MIN_INT
        if result > MAX_INT: return MAX_INT
        
        return result 
        
        
        