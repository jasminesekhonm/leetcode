class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        i = 0 

        while i < len(tokens):
            if tokens[i] in operators:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                print(operand1, operand2)
                if tokens[i] == "+":
                    res = operand1 + operand2
                elif tokens[i] == "-":
                    res = operand2 - operand1
                elif tokens[i] == "*":
                    res = operand1 * operand2
                elif tokens[i] == "/":
                    res = operand2/operand1    
                stack.append(int(res))
                i += 1
            else:
                stack.append(int(tokens[i]))
                i += 1
        
        return stack.pop()


        
