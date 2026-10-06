class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxPos, maxNeg = 1, 1
        for num in nums:
            if num == 0:
                maxPos, maxNeg = 1, 1
                res = max(num, res)
                continue
            temp = maxPos
            maxPos = max(num, num * maxPos, num * maxNeg)
            maxNeg = min(num, num * temp, num * maxNeg)
            res = max(maxPos, res)
        return res
