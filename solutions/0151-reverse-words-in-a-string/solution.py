class Solution:
    def reverseWords(self, s: str) -> str:
        wordStack = []
        currWord = ""
        for char in s:
            if char.isalnum():
                currWord=currWord+char 
            elif len(currWord) > 0:
                wordStack.append(currWord)
                currWord=""
        if len(currWord) > 0:
            wordStack.append(currWord)
        res = ""
        while wordStack:
            currWord = wordStack.pop()
            res = res+currWord 
            if len(wordStack) > 0:
                res = res + " "
        
        return res 

