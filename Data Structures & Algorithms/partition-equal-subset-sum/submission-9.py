class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        dp, target = set([0]), total / 2
        for num in nums:
            for elem in list(dp):
                newElem = num + elem
                if newElem == target:
                    return True
                dp.add(newElem)
        return False