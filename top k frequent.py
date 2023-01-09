class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dct = {}
        stack = []
        output = []
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        
        for i in dct:
            stack.append((i,dct[i]))
        
        stack = sorted(stack,key=lambda x: x[1])

        for i in range(1,k+1):
            num = stack.pop()
            output.append(num[0])
            
        return output