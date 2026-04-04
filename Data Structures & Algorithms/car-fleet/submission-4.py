class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = dict()
        stack = []
        for i in range(len(position)):
            pair[position[i]] = speed[i]
        position.sort()
        for pos in position[::-1]:
            vel = (target - pos) / pair[pos]
            stack.append(vel)
            if(len(stack)==1):
                continue;
            elif(vel<=stack[len(stack)-2]):
                stack.pop()
        return len(stack)