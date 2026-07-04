class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == "+":
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(x + y)
            elif tok == "-":
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(y - x)
            elif tok == "*":
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(x * y)
            elif tok == "/":
                x, y = int(stack.pop()), int(stack.pop())
                print(x, y)
                stack.append(int(y/x))
            else:
                stack.append(tok)
        return int(stack[0])