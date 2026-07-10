class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freqDict = {}
        maxFreq = 0
        for r in range(len(s)):
            freqDict[s[r]] = 1 + freqDict.get(s[r], 0)
            maxFreq = max(maxFreq, freqDict[s[r]])
            while (r - l + 1) - maxFreq > k:
                freqDict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res