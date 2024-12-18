class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = { val:i for i, val in enumerate(nums1)}
        result = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in hashMap:
                continue

            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    indx = hashMap[nums2[i]]
                    result[indx] = nums2[j]
                    break

        return result

        