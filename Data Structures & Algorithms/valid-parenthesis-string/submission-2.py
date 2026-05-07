class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin+1, leftMax+1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            leftMin = leftMin if leftMin >= 0 else 0
            if leftMax < 0:
                return False
        return True if leftMin == 0 else False
        