class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
            
        index = 0
        for item in t:
            if s and item == s[index]:
                index += 1
                if index == len(s):
                    return True
        
        return False