from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        stack = deque()
        
        i = 0

        while i < len(tokens):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    stack.append(a+b)
                elif tokens[i] == '-':
                    stack.append(a-b)
                elif tokens[i] == '*':
                    stack.append(a*b)
                elif tokens[i] == '/':
                    stack.append(int(a/b))
            i += 1
        return stack[0]
                
                        
            