class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        l = 0 
        maxLen = 0
        maxFreq = 0
        for r in range(len(s)):
            dictionary[s[r]] = 1 + dictionary.get(s[r],0)
            maxFreq = max(maxFreq, dictionary[s[r]])
            windowLen = r-l+1
            while windowLen-maxFreq>k:
                dictionary[s[l]]-=1
                l+=1
            maxLen = max(maxLen, widowLen)
            
