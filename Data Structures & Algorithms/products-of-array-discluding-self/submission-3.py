class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = 1
        for p in range(1,len(nums)):
            prefix[p]=prefix[p-1]*nums[p-1]
        suffix = [0] * len(nums)
        suffix[-1] = 1
        for s in range(len(nums)-2,-1,-1):
            suffix[s]=suffix[s+1]*nums[s+1]
        res = [0] * len(nums)
        print(prefix)
        print(suffix)
        for k in range(len(nums)):
            res[k] = prefix[k]*suffix[k]
        return res
