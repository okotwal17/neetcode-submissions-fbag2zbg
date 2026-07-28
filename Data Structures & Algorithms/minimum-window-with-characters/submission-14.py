class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        tFreq = {}
        for c in t:
            tFreq[c] = 1 + tFreq.get(c, 0)
        sFreq = {}
        have, need = 0, len(tFreq)
        minWindowLen = float("inf")
        minWindowStr = (-1, -1)
        l = 0
        for r in range(len(s)):
            print(s[l: r+1])
            if s[r] in tFreq:
                sFreq[s[r]] = 1 + sFreq.get(s[r], 0)
                if sFreq[s[r]] == tFreq[s[r]]:
                    have += 1
            while have == need:
                if r - l + 1 < minWindowLen:
                    minWindowLen = r - l + 1
                    minWindowStr = (l,r)
                if s[l] in tFreq:
                    sFreq[s[l]] -= 1
                    if sFreq[s[l]] < tFreq[s[l]]:
                        have -= 1
                l += 1
        return s[minWindowStr[0]: minWindowStr[1] + 1] if minWindowLen != float("inf") else ""