class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        res = [0] * len(nums)
        suffix = [1] * len(nums)
        for a in range(1,len(nums)):
            prefix[a] = prefix[a-1] * nums[a-1]
        for b in range(len(nums)-2,-1,-1):
            suffix[b]= suffix[b+1] * nums[b+1]
        for c in range(len(nums)):
            res[c] = prefix[c] * suffix[c]
        return res