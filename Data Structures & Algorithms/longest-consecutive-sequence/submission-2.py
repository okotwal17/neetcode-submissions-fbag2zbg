class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0;
        elements = set()
        for element in nums:
            elements.add(element);
        for i in range(len(nums)):
            local = 0;
            currNum = nums[i]
            if(nums[i]-1 not in elements):
                local+=1
                currNum = nums[i]
                while(currNum+1 in elements):
                    local+=1
                    currNum+=1
                if(local>longest):
                    longest = local
        return longest