class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) == abs(a):
                    stack.pop()
                elif abs(stack[-1]) <= abs(a):
                    stack.pop()
                    stack.append(a)
            else:
                stack.append(a)
        return stack
