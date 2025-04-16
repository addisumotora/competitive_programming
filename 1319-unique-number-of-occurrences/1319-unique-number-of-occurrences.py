class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        seen = set()

        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
          
    
        for num, value in count.items():
            if value in seen:
                return False
            else:
                seen.add(value)
        
        return True
