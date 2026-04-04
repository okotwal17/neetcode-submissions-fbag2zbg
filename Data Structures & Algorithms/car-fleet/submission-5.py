class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = dict()
        stack = []
        for i in range(len(position)):
            pair[position[i]] = speed[i]
        
        position.sort()

        for pos in position[::-1]:
            pastSpeed = -1
            if(len(stack)>=1):
                pastSpeed = stack[-1]
            velocity = (target - pos) / pair[pos]
            stack.append(velocity)
            if(pastSpeed == -1):
                continue
            elif(velocity<=pastSpeed):
                stack.pop()

        return len(stack)