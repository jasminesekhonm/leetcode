class Solution:
    def isValid(self, s: str) -> bool:
        bracketDict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for char in s:
            if char in list(bracketDict.keys()):
                stack.append(char)
            elif char in list(bracketDict.values()):
                if len(stack) > 0:
                    lastOpen = stack.pop()
                    if not bracketDict[lastOpen] == char:
                        return False
                else:
                    return False 
        return (True if len(stack) == 0 else False)

        
