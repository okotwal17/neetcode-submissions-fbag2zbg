import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        l, r = 1, maxPiles
        res = -1
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
            

