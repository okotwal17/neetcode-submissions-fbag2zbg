class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = []
        stack = [] 
        for _ in range(len(position)):
            tuples.append((position[_],speed[_]))
        
        position.sort()

        for car in tuples:
            time = (target - car[0])/car[1]
            stack.append(time)
            if (len(stack)==1):
                continue
            elif(time<=stack[len(stack)-2]):
                stack.pop()
        
        return len(stack)