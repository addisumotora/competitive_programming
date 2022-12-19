class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def largest(a,b):
            if a+b>b+a:
                return 0
            elif a+b < b+a:
                return 1
            else:
                return 0


        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if largest(str(nums[j]),str(nums[j+1])):
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        return str(int(''.join(str(i) for i in nums)))