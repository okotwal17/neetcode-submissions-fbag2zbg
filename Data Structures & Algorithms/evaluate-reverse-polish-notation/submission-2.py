class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if(i == "+"):
                num1 = stack.pop()
                num2 = stack.pop()
                print(num1+num2)
                stack.append(num1+num2)
            elif(i == "-"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1-num2)
                print(num1-num2)
            elif(i == "*"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
                print(num1*num2)
            elif(i == "/"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(math.floor(num1/num2))
                print(math.floor(num1/num2))
            else:
                print(i)
                stack.append(int(i))
        return stack.pop()