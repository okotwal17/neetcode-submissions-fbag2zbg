class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        allEle = set()
        for i in nums:
            allEle.add(i)

        longestCount = 1
        for i in range(len(nums)):
            if nums[i] - 1 in allEle:
                count = 2
                temp = nums[i]
                while temp + 1 in allEle:
                    count +=1
                    temp = temp + 1
                longestCount = max(longestCount,count)
        return longestCount
                