class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        #1201
        #1301 
        def dfs(i):
            if i >= len(s):
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == "0":
                return float("inf")
            res1, res2 = float("inf"), float("inf")
            res1 = dfs(i + 1)
            if i + 1 < len(s) and ((s[i] == "1" and s[i+1] in "0123456789") or
            (s[i] == "2" and s[i + 1] in "0123456")):
                res2 = dfs(i + 2)
            if res1 == float("inf") and res2 == float("inf"):
                return float("inf")
            res1 = res1 if res1 != float("inf") else 0
            res2 = res2 if res2 != float("inf") else 0
            dp[i] = res1 + res2
            return dp[i]
        res = dfs(0)
        return res if res != float("inf") else 0
            
            