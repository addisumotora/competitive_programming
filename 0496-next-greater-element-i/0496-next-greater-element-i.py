class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsHashmap = {n:i for i,n in enumerate(nums1) }
        output = [-1] * len(nums1)
        stack = []
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop();
                indx = numsHashmap[val]
                output[indx] = nums2[i]
            if nums2[i] in nums1:
                stack.append(nums2[i])
        return output
        
        
        
        