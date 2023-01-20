class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        counter = 0
        prefixSum = { 0:1 }

        for n in nums:
            total = total + n
            diff = total - k
            
            counter += prefixSum.get(diff,0)
            prefixSum[total] = 1 + prefixSum.get(total,0)
        
        return counter
