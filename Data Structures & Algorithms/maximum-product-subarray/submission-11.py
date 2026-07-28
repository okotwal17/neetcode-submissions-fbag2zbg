class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = curMin = 1
        for n in nums:
            if n == 0:
                curMax = curMin = 1
                continue
            curMax, curMin = max(n, n * curMax, n * curMin), min(n, n * curMax, n * curMin)
            res = max(res, curMax)
        return res