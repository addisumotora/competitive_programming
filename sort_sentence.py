class Solution:
    def sortSentence(self, s: str) -> str:
        stringArray = s.split(' ')
        numsArray = [0]*len(stringArray)
        for i in stringArray:
            index = i[len(i)-1]
            string = i[:-1]
            numsArray[eval(index)-1] = string
        return ' '.join(numsArray)
        
        
        