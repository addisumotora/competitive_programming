class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for _ in range(k):
            min_index = 0
            for j in range(n):
                if nums[j] < nums[min_index]:
                    min_index = j
            
            nums[min_index] = nums[min_index] * multiplier

        return nums
