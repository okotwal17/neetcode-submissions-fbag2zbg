class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        for pair in pairs:
            time = (target - pair[0])/pair[1]
            if stack and stack[-1]>=time:
                stack.pop()
            stack.append(time)
        return len(stack)