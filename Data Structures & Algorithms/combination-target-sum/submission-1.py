class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curSum, path):
            if i >= len(nums) or curSum>target:
                return
            if curSum == target:
                res.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i, curSum + nums[i], path)
            path.pop()
            backtrack(i + 1, curSum, path)
        backtrack(0,0, [])
        return res