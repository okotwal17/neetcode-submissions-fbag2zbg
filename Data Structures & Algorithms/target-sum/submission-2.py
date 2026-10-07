class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        backtracking appraoch, either plus or minus current number move onto next i
        if end and equal return 1
        if end and not equal return 0
        DP approach
        (i, curSum) --> # of ways to get to target
        """
        dp = {}
        def dfs(i, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            if i >= len(nums) and curSum == target:
                return 1
            if i >= len(nums):
                return 0
            dp[(i, curSum)] = dfs(i + 1, curSum - nums[i]) + dfs(i + 1, curSum + nums[i])
            return dp[(i, curSum)]
        return dfs(0,0)
        