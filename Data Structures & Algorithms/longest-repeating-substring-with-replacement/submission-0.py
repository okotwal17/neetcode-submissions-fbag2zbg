class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        l,r = 0,0
        maxLen = 0
        while r<len(s):
            dictionary[s[r]] = 1+dictionary.get(s[r], 0)
            if r-l+1 - dictionary[max(dictionary)] <=k:
                r+=1
                maxLen = max(r-l+1,maxLen)
            else:
                dictionary[s[l]]-=1
                l+=1
        return maxLen-1
            
