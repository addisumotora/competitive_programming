class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans =[0]*len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]]< temperatures[i]:
                n=stack.pop()
                ans[n] = i-n
            stack.append(i)
        return ans