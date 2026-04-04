class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curStr, openN, closeN):
            if openN == closeN == n:
                res.append(curStr)
                return
            if openN < n:
                curStr+='('
                backtrack(curStr, openN + 1, closeN)
                curStr = curStr[:-1]
            if closeN < openN:
                curStr+=')'
                backtrack(curStr, openN, closeN + 1)
        backtrack("",0,0)
        return res
