class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for i in num:

            while stack and stack[-1]> i and k>0:
                stack.pop()
                k-=1
            stack.append(i)

        stack = stack[:len(stack)-k]
        res = ''.join(stack)
        return str(int(res)) if res else "0"