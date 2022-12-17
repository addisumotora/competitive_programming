class Solution:
    def sortSentence(self, s: str) -> str:
        
        sentence  = s.split(' ')
        sortedSentence = [0]*len(sentence)
        
        for i in sentence:
            num = int(i[-1])
            sortedSentence[num-1] = i[:-1]
        return ' '.join(sortedSentence)