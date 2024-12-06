class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        l, r = 0, 0
        n_index = 0

        while r < len(haystack):
            if haystack[r] == needle[n_index]:
                n_index += 1
                if n_index == len(needle):  
                    return l
            else:
                n_index = 0
                l += 1
                r = l - 1  

            r += 1

        return -1