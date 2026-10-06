class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp.get(i, 1), 1 + dfs(j))
            if i not in dp:
                dp[i] = 1
            return dp[i]
        for i in range(len(nums)):
            dfs(i)
        return max(dp.values())


