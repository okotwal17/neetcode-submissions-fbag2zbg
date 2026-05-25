class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, canBuy):
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            if i >= len(prices):
                return 0
            if canBuy:
                dp[(i, canBuy)] = max(dfs(i + 1, canBuy), dfs(i+1, not canBuy) - prices[i])
                return dp[(i, canBuy)]
            dp[(i, canBuy)] = max(dfs(i + 1, canBuy), prices[i] + dfs(i+2, not canBuy))
            return dp[(i, canBuy)]
        return dfs(0, True)
            