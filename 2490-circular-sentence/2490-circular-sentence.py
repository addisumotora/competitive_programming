class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        first_word = sentence[0]
        last_word = sentence[-1]
        
        for i in range(1, len(sentence)):
            item = sentence[i]
            if first_word[-1] != item[0]: 
                return False
            
            first_word = item
            
        print(first_word)
            
        if sentence[0][0] == sentence[-1][-1]:
            return True
        
        return False
            
        
        