import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #First, maxPiles. Max/min eating rate is maximum of the piles to 1
        maxPiles = max(piles)
        l, r = 1, maxPiles
        res = -1
        #Binary search through the rates and eat. If the time is greater than the
        #amount of hours, then increase rate
        #else store the current value and try to decrease it
        while l <= r:
            k = (l + r) // 2
            time = 0
            for pile in piles:
                time+=math.ceil(pile/k)
            if time > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res
            

