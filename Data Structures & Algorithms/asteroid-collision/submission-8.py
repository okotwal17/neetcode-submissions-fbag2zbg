class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                print(stack)
                if abs(stack[-1]) == abs(a):
                    stack.pop()
                    break
                elif abs(stack[-1]) <= abs(a):
                    stack.pop()
                    stack.append(a)
                    print(stack)
                else:
                    break
            else:
                stack.append(a)
                print(stack)
        return stack
