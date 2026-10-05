class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def houseRobber(arr):
            dp = [-1] * len(nums)
            def dfs(i):
                if i >= len(arr):
                    return 0
                if dp[i] != -1:
                    return dp[i]
                dp[i] = max(dfs(i + 1), dfs(i + 2) + arr[i])
                return dp[i]
            return dfs(0)
        return max(houseRobber(nums[:len(nums) - 1]), houseRobber(nums[1:]))
        