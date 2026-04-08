class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        matching = {"[":"]","{":"}","(":")"}
        for c in s:
            if(c in matching):
                stack.append(c)
            else:
                top = stack.pop()
                if (c != matching[top]):
                    return False;
        return True;