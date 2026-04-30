class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = [0] * len(nums)
        curSum[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            curSum[i] = max(curSum[i-1] + nums[i], nums[i])
            res = max(res, curSum[i])
        return res