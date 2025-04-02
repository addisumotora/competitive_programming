class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0

        for char in t:
            if l < len(s) and s[l] == char:
                l += 1

        return l == len(s)
