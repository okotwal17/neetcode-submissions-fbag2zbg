class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(curSum, path, i):
            if curSum == target:
                if path not in res:
                    res.append(path[:])
                return
            if i >= len(candidates) or curSum > target:
                return
            path.append(candidates[i])
            dfs(curSum + candidates[i], path, i + 1)
            path.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(curSum, path, i + 1)
        dfs(0,[],0)
        return res
