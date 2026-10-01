class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        
        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                lastChar = stack.pop()
                if not brackets[lastChar] == char:
                    return False 
        return True if len(stack) == 0 else False
                
        
