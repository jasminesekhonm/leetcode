class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWordLen = 0
        for char in s[::-1]:
            if char == " " and lastWordLen != 0:
                return lastWordLen 
            elif char.isalnum():
                lastWordLen += 1
        return lastWordLen



        
