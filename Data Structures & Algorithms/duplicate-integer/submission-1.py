class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements=set()
        for i in nums:
            if(i in elements):
                return True
            elements.add(i)
        return False