class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreq = {}
        for c in t:
            tFreq[c] = 1 + tFreq.get(c, 0)
        sFreq = {}
        l, r = 0, 0
        have, need = 0,len(tFreq)
        resLen, res = float('inf'), ""
        while r < len(s):
            sFreq[s[r]] = 1 + sFreq.get(s[r], 0)
            if s[r] in tFreq and sFreq[s[r]] == tFreq[s[r]]:
                have += 1
            while have == need:
                print(l, r, sFreq)
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                sFreq[s[l]] -= 1
                if s[l] in tFreq and sFreq[s[l]] < tFreq[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return res if resLen != float('inf') else ""


