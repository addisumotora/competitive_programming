class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n - 1):
            if(nums[i] == nums[i + 1]):
                nums[i] *= 2
                nums[i + 1] = 0
        
        for i in range(n):
            if nums[i] != 0:
                ans.append(nums[i])
        
        for i in range(len(ans), n):
            ans.append(0)

        return ans