class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Keep seeing if windowMax is beat when prices[l] < prices[r]
        l = 0
        res, maxWindowElem = 0, -1
        for r in range(1, len(prices)):
            print(maxWindowElem)
            if prices[l] < prices[r] and maxWindowElem < prices[r]:
                maxWindowElem = prices[r]
            else:
                res += (maxWindowElem - prices[l]) if maxWindowElem != -1 else 0
                maxWindowElem = -1
                l = r
        print(maxWindowElem)
        return res + (maxWindowElem - prices[l]) if maxWindowElem != -1 else res