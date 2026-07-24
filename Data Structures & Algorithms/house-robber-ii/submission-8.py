class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def houseRobber(startIdx, endIdx):
            house1, house2 = 0,0
            for i in range(startIdx, endIdx):
                house1, house2 = house2, max(nums[i] + house1, house2)
            return house2
        return max(houseRobber(1, len(nums)), houseRobber(0, len(nums) - 1))