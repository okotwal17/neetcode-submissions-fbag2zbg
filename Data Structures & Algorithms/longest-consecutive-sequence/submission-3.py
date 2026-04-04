class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collection = set(nums)
        maxLength = 0
        for num in collection:
            if num - 1 not in collection:
                length = 1
                while num + length in collection:
                    length+=1
                maxLength = max(maxLength, length)
        return maxLength