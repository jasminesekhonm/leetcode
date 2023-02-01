class Solution:
    def isValid(self, s: str) -> bool:
        paranthesesDict = {')': '(', 
                            ']': '[', 
                            '}': '{'}
        
        
        stack = []
        for char in s: 
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if len(stack) == 0:
                    return False 
                last_open = stack.pop()
                if last_open != paranthesesDict[char]:
                    return False 
        return True if len(stack) == 0 else False 
