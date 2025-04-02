class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        l = 0

        for r in range(len(t)):
            if l < len(s) and s[l] == t[r]:
                l += 1
            elif l == len(s):
                return True
                
        return True if len(s) == l else False