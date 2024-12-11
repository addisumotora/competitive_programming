class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prodMax = nums[0]
        res = nums[0]
        prodMin = prodMax
        for i in range(1, len(nums)):
            temp = prodMax * nums[i]

            prodMax = max(nums[i] * prodMin,  prodMax * nums[i], nums[i])
            prodMin = min(temp, prodMin * nums[i], nums[i])

            res = max(res, prodMax)
        
        return res