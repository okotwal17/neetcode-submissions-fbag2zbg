class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t == "+":
                res = 0
                while len(stack) != 0:
                    res+=stack.pop()
                stack.append(res)
            elif t == "-":
                res = 0
                while len(stack) != 0:
                    res-=stack.pop()
                stack.append(res)
            elif t == "*":
                res = 1
                while len(stack) != 0:
                    res*=stack.pop()
                stack.append(res)
            elif t == "/":
                res = 1
                while len(stack) != 0:
                    res//=stack.pop()
                stack.append(res)
            else:
                stack.append(int(t))
        return stack.pop()
            