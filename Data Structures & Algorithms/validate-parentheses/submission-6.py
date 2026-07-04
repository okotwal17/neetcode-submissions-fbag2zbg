class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"{" : "}", "[" : "]", "(" : ")"}
        for c in s:
            if c in matches:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                if matches[stack[-1]] != c:
                    return False
                stack.pop()
        return False if len(stack) else True