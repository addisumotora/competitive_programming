class Solution:
    def myPow(self, x: float, n: int) -> float:
        summ = 1
        if n < 0 : 
            x = 1/x
            n = abs(n)

        while n > 0 :
            summ = summ * x
            n -= 1
        return summ

        def helper(x, n):

            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n//2)
            
            res = res * res
            return x * res if n % 2 else res

        res = helper(x,abs(n))

        return res if n >= 0 else 1/res

