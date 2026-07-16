class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(numOpen, numClose, curStr):
            if len(curStr) == n * 2:
                res.append(curStr)
                return
            if numOpen == n:
                curStr += ")"
                dfs(numOpen, numClose + 1, curStr)
            else:
                curStr += "("
                dfs(numOpen + 1, numClose, curStr)
                if numClose < numOpen:
                    curStr = curStr[:-1]
                    curStr += ")"
                    dfs(numOpen, numClose + 1, curStr)
        dfs(0,0, "")
        return res

