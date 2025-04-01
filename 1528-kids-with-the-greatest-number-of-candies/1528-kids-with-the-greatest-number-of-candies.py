class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = [False] * len(candies)
        max_val = max(candies)

        for i, candy in enumerate(candies):
            if candies[i] + extraCandies >= max_val:
                output[i] = True

        return output


