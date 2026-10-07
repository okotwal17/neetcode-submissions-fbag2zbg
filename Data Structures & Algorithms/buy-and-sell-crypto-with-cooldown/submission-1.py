class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            if canBuy:
                dp[(i, canBuy)] = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True), 0)
            else:
                dp[(i, canBuy)] = max(dfs(i + 2, True) + prices[i], dfs(i + 1, False), 0)
            return dp[(i, canBuy)]
        return dfs(0,True)
        
    