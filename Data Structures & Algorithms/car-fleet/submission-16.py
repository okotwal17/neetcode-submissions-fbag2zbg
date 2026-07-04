class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        for pos, vel in zip(position, speed):
            hashmap[pos] = vel
        position.sort(reverse=True)
        stack = []
        for pos in position:
            time = (target - pos) / hashmap[pos]
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)