class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if r > 0 and r < numRows - 1 and i + increment - r * 2 < len(s):
                    res += s[i + increment - r * 2]
        return res
        # for i in range(numRows):
        #     l = i
        #     while l < len(s):
        #         res += s[l]
        #         if i > 0 and i < numRows - 1:
        #             diag_index = l + 2 * (numRows - 1) - 2 * i
        #             if diag_index < len(s): 
        #                 res += s[diag_index]

        #         l += 2 * (numRows - 1)

        # return res