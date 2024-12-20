class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = { "M" :1000, "D":500, "C": 100, "L":50, "X":10 , "V": 5, "I": 1}
        
        s = s.replace('IV', 'IIII') \
             .replace('IX', 'VIIII') \
             .replace('XL', 'XXXX') \
             .replace('XC', 'LXXXX') \
             .replace('CD', 'CCCC') \
             .replace('CM', 'DCCCC')
        
        num = 0 
        for i in s:
            num += num_map[i]
        
        return num
            