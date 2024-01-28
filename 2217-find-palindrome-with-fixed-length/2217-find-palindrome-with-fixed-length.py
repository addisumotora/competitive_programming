class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res = []
        ln = ceil(intLength/2)
        odd = intLength%2 == 1
        base = 10**(ln-1)
 
        for k in queries:
            val = str(k-1+base)
            if len(val)>ln:
                res.append(-1)
            else: res.append(int(val+val[-2::-1])) if odd else res.append(int(val+val[::-1]))
        return res 
        
            