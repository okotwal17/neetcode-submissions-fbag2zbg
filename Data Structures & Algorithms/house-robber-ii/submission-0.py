class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, rob1, rob2):
            for house in nums:
                temp = max(rob1 + house, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(helper(nums[1:],0,0),helper(nums[:-1],0,0))