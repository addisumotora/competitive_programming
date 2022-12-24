class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        for i in nums1:
            flag=False
            index = nums2.index(i)
            for j in nums2[index:]:
                if j>i:
                    stack.append(j)
                    flag=True
                    break        
            if not flag:
                stack.append(-1)
        return stack