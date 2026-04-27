class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        negative = False
        if n < 0:
            n*=-1
            negative = True
        for i in range(n):
            res*=x
        return res if not negative else 1/res