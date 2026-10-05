class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(path, i, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if curSum > target or i >= len(candidates):
                return
            path.append(candidates[i])
            dfs(path, i + 1, curSum + candidates[i])
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(path, i + 1, curSum)
        dfs([], 0, 0)
        return res