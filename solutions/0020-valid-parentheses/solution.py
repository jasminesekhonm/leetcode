class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False 
        
        q = []
        opening_brackets = {'(': 0, '{': 1, '[': 2}
        closing_brackets = {')': 0, '}': 1, ']': 2}
        
        if s[0] in list(closing_brackets.keys()):
            return False 
        
        for i in range(len(s)):
            if s[i] in list(opening_brackets.keys()):
                q.append(opening_brackets[s[i]])
            elif s[i] in list(closing_brackets.keys()):
                if len(q) == 0:
                    return False
                opening_last = q.pop()
                closing_last = closing_brackets[s[i]]
                if closing_last != opening_last:
                    return False 
        if len(q) != 0:
            return False
        return True
                
                
                
            
            
        
