class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(numOpen, numClose, curStr):
            if len(curStr) == n * 2:
                res.append(curStr)
                return
            if numOpen < n:
                dfs(numOpen + 1, numClose, curStr + "(")
            if numClose < numOpen:
                dfs(numOpen, numClose + 1, curStr + ")")
        dfs(0,0, "")
        return res

