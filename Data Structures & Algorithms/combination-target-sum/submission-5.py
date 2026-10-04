class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(path, i, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if curSum > target or i >= len(nums):
                return
            path.append(nums[i])
            dfs(path, i, curSum + nums[i])
            path.pop()
            dfs(path, i + 1, curSum)
        dfs([], 0, 0)
        return res