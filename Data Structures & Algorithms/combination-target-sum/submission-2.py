class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, path, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if index >= len(nums) or curSum > target:
                return

            path.append(nums[index])
            backtrack(index, path, curSum + nums[index])
            path.pop()
            backtrack(index + 1, path, curSum)
        backtrack(0,[],0)
        return res