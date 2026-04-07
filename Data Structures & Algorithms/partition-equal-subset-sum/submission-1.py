class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        s = set()
        s.add(0)
        target = sum(nums)/2
        for i in range(len(nums) - 1, -1 , -1):
            nextS = set()
            for t in s:
                if t + nums[i] == target:
                    return True
                nextS.add(t + nums[i]) if t + nums[i] <= target else None
                nextS.add(t)
            s = nextS
        return False            