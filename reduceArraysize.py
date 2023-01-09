class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        count = 0
        dct = {}
        stack = []
        n = len(arr)
        for i in arr:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        for i in dct:
            stack.append(dct[i])
        
        stack = sorted(stack)
        
        temp=0

        for i in range(len(stack)-1,-1,-1):
            if stack[i] > n//2:
                return 1
            if temp < n//2:
                count+=1
                temp = temp + stack[i]
            if temp >= n//2:
                return count