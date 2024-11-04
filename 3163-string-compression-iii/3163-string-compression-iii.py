class Solution:
    def compressedString(self, word: str) -> str:
        
        ch = word[0]
        count = 1
        comp = ''
        
        for item in word[1:]:
            if count == 9:
                comp += str(9)+ch
                count = 0
            
            if ch != item and count != 0:
                comp += str(count) + ch
                count = 0
                
            ch = item
            count += 1
            
            
        comp += str(count) + ch
        
        return comp
            
            