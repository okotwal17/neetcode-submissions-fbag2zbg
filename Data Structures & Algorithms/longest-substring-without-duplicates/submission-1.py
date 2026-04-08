class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        elements = set()
        while l<len(s):
            print(s[l])
            print(elements)
            if(s[l] in elements):
                if(len(elements)>longest):
                    longest = len(elements)
                elements.clear()
            elements.add(s[l])
            l+=1
        if(len(elements)>longest):
            longest = len(elements)
        return longest

    