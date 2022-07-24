class Solution:
    def isValid(self, s: str) -> bool:
        # s = '({[]})'
        if len(s) <= 1:
            return False 
        
        stack = []
        opening_brackets = {'(': 1, '{': 2, '[': 3}
        closing_brackets = {')': 1, '}': 2, ']':3}
        i = 0
        while i < len(s):
            if s[i] in list(opening_brackets.keys()):
                stack.append(opening_brackets[s[i]])
            elif s[i] in list(closing_brackets.keys()):
                if len(stack) == 0:
                    return False
                open_brack = stack.pop()
                if closing_brackets[s[i]] != open_brack:
                    return False
            i = i + 1
        if len(stack) != 0:
            return False
        return True
                    
                
        
