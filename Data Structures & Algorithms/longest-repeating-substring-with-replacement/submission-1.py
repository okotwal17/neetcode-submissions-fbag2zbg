class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        l,r = 0,0
        maxLen = 0
        while r<len(s):
            dictionary[s[r]] = 1+dictionary.get(s[r], 0)
            windowLen = r-l+1
            if windowLen - dictionary[max(dictionary)] <=k:
                maxLen = max(r-l+1,maxLen)
                r+=1
            else:
                dictionary[s[l]]-=1
                l+=1
        return maxLen
            
