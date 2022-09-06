class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        newS = ""
        newT = ""
        
        def findStr(string):
            newStr = []
            i = len(string)-1
            skipChars = 0
            for char in reversed(string):
                if char == '#':
                    skipChars += 1
                elif skipChars > 0:
                    skipChars -= 1
                elif skipChars == 0:
                    newStr.append(char)
            return newStr[::-1]
        
        return findStr(s) == findStr(t)
                    
