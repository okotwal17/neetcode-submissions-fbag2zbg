class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = 1
        for a in range(1,n):
            prefix[a] = prefix[a-1]*nums[a-1]
        suffix = [0] * n
        suffix[-1] = 1
        for b in range(n-2,-1,-1):
            suffix[b] = suffix[b+1] * nums[b+1]
        res = [0]*n
        for c in range(n):
            res[c] = prefix[c]*suffix[c]
        return res

