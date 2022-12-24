class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            isg = False
            isgg = False
            for j in nums2:
                if j == i:
                    isg = True
                if isg and j>i:
                    ans.append(j)
                    isgg = True
                    break
            if not isgg:
                ans.append(-1)
        return ans