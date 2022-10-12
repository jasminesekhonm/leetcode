class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lenLongest = 0
        stack = [-1]
        currLen = 0
        for i, val in enumerate(s):
            if val == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    lenLongest = max(lenLongest, i - stack[-1])
                   
        return lenLongest
                    
        
