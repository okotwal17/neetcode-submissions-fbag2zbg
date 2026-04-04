class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, arrBool):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not arrBool[i]:
                    arrBool[i] = True
                    path.append(nums[i])
                    backtrack(path, arrBool)
                    arrBool[i] = False
                    path.pop()


        backtrack([], [False] * len(nums))
        return res