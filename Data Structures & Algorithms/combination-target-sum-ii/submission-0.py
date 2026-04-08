class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, curSum, path):
            if path in res:
                return
            if curSum == target:
                res.append(path[:])
                return
            if index >= len(candidates) or curSum>target:
                return
            
            path.append(candidates[index])
            backtrack(index + 1, curSum + candidates[index], path)
            path.pop()
            backtrack(index + 1, curSum, path)
        backtrack(0, 0,[])
        return res