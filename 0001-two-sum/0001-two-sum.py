class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        map[nums[0]] = 0

        for i in range(1,len(nums)):
            diff = target - nums[i]

            if diff in map:
                return [map[diff], i]

            map[nums[i]] = i
