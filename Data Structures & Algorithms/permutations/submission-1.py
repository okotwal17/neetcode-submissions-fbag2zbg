class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, boolArr):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not boolArr[i]:
                    path.append(nums[i])
                    boolArr[i] = True
                    backtrack(path, boolArr)
                    path.pop()
                    boolArr[i] = False
        backtrack([], [False] * len(nums))
        return res