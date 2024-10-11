class Solution:
    def intToRoman(self, num: int) -> str:
        mydict = {1000 : "M", 900 : "CM", 500 : "D",
                            400 : "CD", 100 : "C", 90: "XC", 50 : "L", 40 : "XL", 
                            10 : "X", 9 : "IX", 5 : "V", 4 : "IV",1 : "I"}
        roman=''
        print(enumerate(mydict))
        for key, value in mydict.items():
            while key <= num:
                roman += value
                num -= key
                
        return roman;
                