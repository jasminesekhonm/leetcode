class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        slen, plen = len(s), len(part)
        if len(part) == 0:
            return s
        if len(s) < len(part):
            return s 
        if s == part:
            return ""
        
        i, j = 0, 0 
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= plen and "".join(stack[-plen:]) == part:
                for _ in range(plen):
                    stack.pop()
        
        return "".join(stack)
