from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        hashmapT = defaultdict(int)
        hashmapS = defaultdict(int)
        for i in t:
            hashmapT[i] += 1
        res, resLen = [-1,-1], len(s) + 1 
        have, need = 0, len(hashmapT)
        l = 0
        for r in range(len(s)):
            hashmapS[s[r]] += 1
            if s[r] in hashmapT and hashmapS[s[r]] == hashmapT[s[r]]:
                have+=1
            while have == need:
                if r-l+1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                hashmapS[s[l]]-=1
                if s[l] in hashmapT and hashmapS[s[l]] < hashmapT[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if resLen != len(s)+1 else ""
        