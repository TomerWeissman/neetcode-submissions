class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                if a < 0 and b < 0:
                    stack.append((-a)//(-b))
                elif b < 0:
                    stack.append(-(a//(-b)))
                elif a < 0:
                    stack.append(-((-a)//b))
                else:
                    stack.append(a//b)

            else:
                stack.append(int(token))

        
        return stack[-1]


        