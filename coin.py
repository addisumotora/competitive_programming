class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l, r = 0, len(piles)
        piles.sort()
        stack = []
        while l < r:
            r-=2
            stack.append(piles[r])
            l+=1
        summ = 0
        for i in stack:
            summ = summ + i

        return summ