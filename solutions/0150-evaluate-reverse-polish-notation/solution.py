class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        q = []
        
        operators = ['+', '-', '*', '/']
        
        
        for token in tokens:
            if token in operators:
                operand1 = q.pop()
                operand2 = q.pop()
                print(token, operand1, operand2)
                
                if token == '+':
                    q.append(operand1 + operand2)
                elif token == '-':
                    q.append(operand2 - operand1)
                elif token == '*':
                    q.append(operand1 * operand2)
                elif token == '/':
                    q.append(int(operand2 / operand1))
            else:
                q.append(int(token))
            #print(token, q)
            
        return sum(q)
                    
                    
                    
                
