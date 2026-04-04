class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maximum = 0
        while(r<len(prices)):
            if(prices[l]>prices[r]):
                l=r
            elif(prices[r]-prices[l]>maximum):
                maximum = prices[r]-prices[l]
            r+=1
        return maximum

