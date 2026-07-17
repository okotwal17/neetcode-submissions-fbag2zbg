class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, path, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if curSum > target or i >= len(candidates):
                return
            path.append(candidates[i])
            backtrack(i + 1, path, curSum + candidates[i])
            path.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i + 1, path, curSum)
        backtrack(0, [], 0)
        return res