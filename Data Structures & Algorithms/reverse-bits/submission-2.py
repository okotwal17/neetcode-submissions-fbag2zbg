class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            pos = (n>>i) & 1
            res = res | (pos << (31 - i))
        return res