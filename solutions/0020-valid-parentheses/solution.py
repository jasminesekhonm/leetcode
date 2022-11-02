class Solution:
    def isValid(self, s: str) -> bool:
        bracketsDict = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for char in s:
            if char in bracketsDict:
                stack.append(char)
            elif char in bracketsDict.values():
                if len(stack) == 0:
                    return False
                openingBracket = stack.pop()
                if not bracketsDict[openingBracket] == char:
                    return False 
        return True if len(stack) == 0 else False
        
