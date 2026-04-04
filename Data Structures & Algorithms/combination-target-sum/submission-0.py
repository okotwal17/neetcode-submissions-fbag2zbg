class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, path,cur_sum):
            if index >= len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                res.append(path[:])
                return
            path.append(nums[index])
            backtrack(index, path, cur_sum + nums[index])
            path.pop()
            backtrack(index + 1, path, cur_sum)
        backtrack(0, [], 0)
        return res
