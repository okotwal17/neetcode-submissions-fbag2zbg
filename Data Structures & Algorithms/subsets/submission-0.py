class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, index):
            print(path, index)
            if index == len(nums):
                res.append(path[:])
                return
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            backtrack(path, index + 1)
        backtrack([],0)
        return res