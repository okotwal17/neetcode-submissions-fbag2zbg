class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set()
        longest_sequence = 0
        for i in nums:
            elements.add(i)
        longest_sequence = 0
        for i in nums:
            local = 0
            if i-1 not in set():
                local += 1
                temp = i
                while(temp+1 in elements):
                    local+=1
                    temp+=1
                if(local > longest_sequence):
                    longest_sequence = local
        return longest_sequence