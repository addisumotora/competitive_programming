class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, 0

        sum_to_k = 0
        av = 0

        for i in range(k):
            sum_to_k += nums[i]
        
        av = sum_to_k / k

        for i in range(k, len(nums)):
            sum_to_k += nums[i]
            
            sum_to_k -= nums[l]

            av = max(av, sum_to_k / k)

            l += 1

        return av 