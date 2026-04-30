class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxPrev = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            maxPrev = max(maxPrev + nums[i], nums[i])
            res = max(res, maxPrev)
        return res