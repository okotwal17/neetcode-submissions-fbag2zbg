class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, curSum, path):
            if curSum == target:
                res.append(path[:])
                return
            if i>=len(candidates) or curSum > target:
                return
            path.append(candidates[i])
            backtrack(i + 1, curSum + candidates[i], path)
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i+=1
            backtrack(i + 1, curSum, path)
        backtrack(0,0,[])
        return res