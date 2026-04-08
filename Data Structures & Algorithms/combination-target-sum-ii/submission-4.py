class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index, path, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if index >= len(candidates):
                return
            path.append(candidates[index])
            backtrack(index + 1, path, curSum + candidates[index])
            path.pop() 
            while index + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                index += 1
            backtrack(index + 1, path, curSum)
        backtrack(0, [], 0)
        return res