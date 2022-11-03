class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        # 2 -> 1, 1
        # 3 -> 2 1 
        # 4 -> 12 and 11
        strVal = self.countAndSay(n - 1)
        print(strVal)
        res = ''
        char = strVal[0]
        charCount = 0
        i = 0
        while i < len(strVal):
            
            while i < len(strVal) and strVal[i] == char:
                charCount += 1
                i += 1
            res = res + str(charCount) + char
            if i < len(strVal):
                char = strVal[i]
                charCount = 0
        return res 
                
            
