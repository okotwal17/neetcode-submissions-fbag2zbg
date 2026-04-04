class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curStr, closeNum, openNum):
            if openNum == closeNum == n:
                res.append(curStr)
                return
            if openNum < n:
                curStr+='('
                backtrack(curStr, closeNum, openNum + 1)
                curStr = curStr[:-1]
            if closeNum < openNum:
                curStr+=')'
                backtrack(curStr, closeNum + 1, openNum)
                curStr = curStr[:-1]
        backtrack("", 0, 0)
        return res
        