class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = dict()
        stack = [] 
        for i in range(len(position)):
            pair[position[i]] = speed[i]

        position.sort()

        for pos in position[::-1]:
            time = (target - pos)/pair[pos]
            print(time)
            stack.append(time)
            if len(stack)==1:
                continue
            elif time<=stack[len(stack)-2]:
                stack.pop()
        
        return len(stack)