class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1,len(prices)):
            print(prices[l], prices[r])
            profit = prices[r] - prices[l]
            print(profit)
            res = max(res, prices[r] - prices[l])
            if profit < 0:
                l=r
        return res