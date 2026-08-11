class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total / 2
        subsets = set()
        subsets.add(0)
        for num in nums:
            for elem in list(subsets):
                if elem + num == half:
                    return True
                subsets.add(elem + num)
        return False