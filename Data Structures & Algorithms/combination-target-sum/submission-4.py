class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curSum, i, path):
            if curSum == target:
                res.append(path[:])
                return
            elif curSum > target or i == len(nums):
                return
            else:
                path.append(nums[i])
                dfs(curSum + nums[i], i, path)
                path.pop()
                dfs(curSum, i + 1, path)
        dfs(0, 0, [])
        return res
