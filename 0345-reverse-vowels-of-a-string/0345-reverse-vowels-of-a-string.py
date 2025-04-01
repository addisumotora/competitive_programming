class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set({
            'a', 'e', 'i', 'o','u'
        })
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() in vowels and s[r].lower() in vowels:
                print(s[l], s[r])
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l].lower() in vowels:
                r -= 1
            elif s[r].lower() in vowels:
                l += 1
            else: 
                l += 1
                r -= 1

        return ''.join(s)
 