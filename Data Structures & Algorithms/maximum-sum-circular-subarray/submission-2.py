class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, maximum = float("-inf"), float("-inf")
        curMin, minimum = float("inf"), float("inf")
        total = 0
        for num in nums:
            total += num
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            maximum = max(curMax, maximum)
            minimum = min(curMin, minimum)
        if maximum < 0:
            return max(nums)
        return max(maximum, total - minimum)