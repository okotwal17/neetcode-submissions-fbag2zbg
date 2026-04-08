class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if(i == "+"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif(i == "-"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1-num2)
            elif(i == "*"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            elif(i == "/"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(math.floor(num1/num2))
            else:
                print(stack)
                stack.append(int(i))
                print(stack)
        return stack.pop()