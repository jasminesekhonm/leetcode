class Solution:
    def reverseWords(self, s: str) -> str:
        
        i = 0
        currWord = ""
        res = ""
        while i <= len(s):
            if i < len(s) and s[i].isalnum():
                currWord = currWord + s[i]
            else:
                if currWord != "":
                    res = currWord + (" " if len(res) > 0 else "") + res
                currWord = ""
            i += 1
        
        return res
            
            
            
            
