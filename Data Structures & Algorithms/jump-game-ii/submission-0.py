class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        curMax = 0
        while r < len(nums) - 1:
            maxDistance = l
            while l <= r:
                maxDistance = max(maxDistance, nums[l]+l)
                l+=1
            curMax+=1
            l = r + 1
            r = maxDistance
        return curMax
            