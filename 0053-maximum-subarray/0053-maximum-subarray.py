class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum  = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if sum + nums[i] <= nums[i]:
                sum = nums[i]
            else:
                sum = sum + nums[i]

            res = max(res, sum)

        return res
        

            
