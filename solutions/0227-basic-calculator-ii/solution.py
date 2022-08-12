class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operation = None
        operand = 0
        sign = 1
        
        for i in range(len(s) + 1):
            char = s[i] if i < len(s) else None  
            if not char is None and char.isdigit():
                operand = operand * 10 + int(char)
            if char is None or char in ['+', '-', '*', '/']:
                if operation in ['*', '/']:
                    last_operand = stack.pop()
                    operand = last_operand / operand if operation == '/' else last_operand * operand 
                    operand = int(operand)
                stack.append(sign * operand)
                operation=char 
                operand=0
                sign=-1 if char == '-' else 1
        
        return sum(stack)
                
                
                    
            
            
                
        
