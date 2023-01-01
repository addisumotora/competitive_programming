class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 3 and n==1:
            return True 
        if n < 3 and n!=1:
            return False
        if n >= 3:
            n = n/3
            return self.isPowerOfThree(n)