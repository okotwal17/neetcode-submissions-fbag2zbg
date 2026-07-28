class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curMax = curMin = nums[0]
        for i in range(1,len(nums)):
            curMax, curMin = max(nums[i], nums[i] * curMax, nums[i] * curMin), min(nums[i], nums[i] * curMax, nums[i] * curMin)
            res = max(res, curMax)
        return res