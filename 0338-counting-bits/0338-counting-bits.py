class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0 
            while i:
                if i & 1:
                    count += 1
                i >>= 1

            res.append(count)

        return res