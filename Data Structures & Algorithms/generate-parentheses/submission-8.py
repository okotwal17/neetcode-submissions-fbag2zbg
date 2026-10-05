class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(numOpen, numClose, path):
            if numOpen == n and numClose == n:
                res.append("".join(path))
                return
            if numOpen == n:
                path.append(")")
                dfs(numOpen, numClose + 1, path)
                path.pop()
                return
            if numOpen == numClose:
                path.append("(")
                dfs(numOpen + 1, numClose, path)
                path.pop()
                return
            path.append("(")
            dfs(numOpen + 1, numClose, path)
            path.pop()
            path.append(")")
            dfs(numOpen, numClose + 1, path)
            path.pop()
        dfs(0,0, [])
        return res