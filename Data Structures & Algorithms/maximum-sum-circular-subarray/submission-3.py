class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = float("-inf")
        curMin = float("inf")
        maximum = float("-inf")
        minimum = float("inf")
        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            maximum = max(curMax, maximum)
            minimum = min(minimum, curMin)

        total = sum(nums)
        if total - minimum == 0:
            return max(nums)
        print(minimum, maximum)
        return max(total - minimum, maximum)