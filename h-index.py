class Solution:
    def hIndex(self, citations: List[int]) -> int:

       citations.sort()
       lenth = len(citations)

       for i in range(lenth):
            if lenth-i <= citations[i]:
                return lenth-i
            
       return 0