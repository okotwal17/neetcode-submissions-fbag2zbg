class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        l = 0
        res = 0
        for r in range(len(s)):
            freqDict[s[r]] = 1 + freqDict.get(s[r], 0)
            while r - l + 1 - max(freqDict.values()) > k:
                freqDict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
