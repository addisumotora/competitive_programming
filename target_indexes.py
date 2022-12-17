class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedNum = sorted(nums)
        index = []
        
        for i in range(len(sortedNum)):
            if sortedNum[i] == target:
                index.append(i)
        return index