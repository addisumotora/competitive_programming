class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     nums.insert(0,nums.pop()) 
        # return nums
        n = len(nums)
        stack = [0] * n
        
        for i in range(n):
            stack[(k+i)%n] = nums[i]
            print((k+i)%n)
        
        for i in range(len(stack)):
            nums[i] = stack[i]