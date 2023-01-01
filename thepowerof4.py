class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n < 4 and n==1:
            return True 
        if n < 4 and n!=1:
            return False
        if n >= 4:
            n = n/4
            return self.isPowerOfFour(n)