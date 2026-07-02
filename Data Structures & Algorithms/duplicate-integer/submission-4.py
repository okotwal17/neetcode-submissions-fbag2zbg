class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allNum = set()
        for i in range(len(nums)):
            if nums[i] in allNum:
                return True
            allNum.add(nums[i])
        return False
