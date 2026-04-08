class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if stack and stack[-1] * a < 0:
                if abs(stack[-1]) <= abs(a):
                    stack.pop()
            else:
                stack.append(a)
        return stack
