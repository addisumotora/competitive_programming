class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r] + num

                if abs(sum - target) < abs(res - target):
                    res = sum

                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return sum
        
        return res
