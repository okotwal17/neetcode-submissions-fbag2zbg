class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack)>=2 and stack[-1]<0 and stack[-2]>0:
                if abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(stack[-2]):
                    temp = stack.pop()
                    stack.pop()
                    stack.append(temp)
                else:
                    stack.pop()
                    break
        return stack