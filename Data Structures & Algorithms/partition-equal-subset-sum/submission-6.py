class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)):
            for t in list(dp):
                if t + nums[i] == target:
                    return True
                dp.add(t + nums[i])
        return target in dp