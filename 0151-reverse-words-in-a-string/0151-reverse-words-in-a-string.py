class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        res = ''
        for word in s[::-1]:
            if word != '':
                res += word + ' '
        
        return res[:-1]
