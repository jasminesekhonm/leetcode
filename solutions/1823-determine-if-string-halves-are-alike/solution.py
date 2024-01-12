class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        slen = len(s)
        acceptedChars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(slen):
            if s[i] in acceptedChars:
                count = count + 1 if i < slen//2 else count - 1
        return (count == 0)


        
