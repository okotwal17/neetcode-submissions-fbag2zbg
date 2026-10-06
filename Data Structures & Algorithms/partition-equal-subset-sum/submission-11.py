class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total / 2
        runningSums = set([0])
        for i in range(len(nums)):
            newSet = runningSums.copy()
            for elem in runningSums:
                if nums[i] + elem == target:
                    return True
                if nums[i] + elem < target:
                    newSet.add(nums[i] + elem)
            runningSums = newSet
        return False