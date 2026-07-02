class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        postfix = [0] * n
        postfix[-1] = 1
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i + 1]
        res = [0] * n
        print(prefix)
        print(postfix)
        for i in range(n):
            res[i] = postfix[i] * prefix[i]
        return res