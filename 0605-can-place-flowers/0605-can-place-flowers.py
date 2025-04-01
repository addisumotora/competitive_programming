class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        length = len(flowerbed)
        while p < length and n > 0:
            if flowerbed[p] == 1:
                p += 2 
            
            elif flowerbed[p] == 0 and (p == length - 1 or flowerbed[p + 1] == 0):
                flowerbed[p] = 1
                p += 2
                n -= 1
            else:
                p += 1

        return n == 0
            
