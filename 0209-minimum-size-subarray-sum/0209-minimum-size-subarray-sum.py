class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        result = 0
        for r in range(len(nums)):
            result += nums[r]
            
            while result >= target:
                res = min(res, r - l + 1)
                result -= nums[l]
                l += 1

        return res if res != float('inf') else 0
