class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total  = 0
        left = 0
        for i in nums:
            total += i

        for i in range(len(nums)):
            right = total - nums[i] - left

            if left == right:
                return i

            left = left + nums[i]
            
        return -1