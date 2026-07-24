class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            print(i)
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            returnVal = cost[i] + min(dfs(i + 1), dfs(i + 2))
            dp[i] = returnVal
            return returnVal
        return min(dfs(0), dfs(1))

        top, bottom = 0, cost[-1]
        for i in range(n - 2):
            top, bottom = bottom, cost[i] + min(top, bottom)
        return min(top, bottom)
        