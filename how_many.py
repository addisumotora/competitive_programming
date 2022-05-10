class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        storeNumber = []
        
        for num in nums:
            count = 0
            for othernums in nums:
                if num>othernums:
                    count+=1
            storeNumber.append(count)
        return storeNumber