class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        subsSet = set()
        for i in range(len(s)):
            while s[i] in subsSet:
                subsSet.remove(s[l])
                l += 1
                
            subsSet.add(s[i])
            res = max(res, i - l + 1)
        
        return res