class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = []
        for i in range(n):
            item = prices[i]
            j = i + 1
            
            while j < n:
                if item >= prices[j]:
                    item -= prices[j]
                    break
                j += 1

            result.append(item)

        return result