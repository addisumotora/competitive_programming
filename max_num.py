class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        di = {}
        count=0

        for i in nums:
            if di.get(k-i,0):
                di[k-i]-=1
                count += 1
            else:
                di[i] = di.get(i, 0) + 1

        return count