class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pastElems = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in pastElems:
                longestSeq, curElem = 1, nums[i]
                while curElem + 1 in pastElems:
                    longestSeq+=1
                    curElem+=1
                res = max(res,longestSeq)
        return res
