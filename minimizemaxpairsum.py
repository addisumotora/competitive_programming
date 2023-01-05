class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        l , r = 0 , len(nums)-1
        maxpair = 0
        while l < r :
            if nums[l] + nums[r] > maxpair:
                maxpair = nums[l] + nums[r]
            
            l += 1
            r -= 1
        
        return maxpair