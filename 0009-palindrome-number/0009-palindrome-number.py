class Solution:
    def isPalindrome(self, x: int) -> bool:
        palendrome = 0
        num = x
        
        if(x < 0): return False
        
        while num > 0:
            n = num % 10
            num = num//10
            palendrome = palendrome * 10 + n
        
        if(palendrome == x): return True
        