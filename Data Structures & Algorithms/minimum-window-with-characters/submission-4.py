from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        hashmapT = defaultdict(int)
        hashmapS = defaultdict(int)
        for i in t:
            hashmapT[i]+=1
        l, r = 0, 0 
        res = [-1,-1]
        bestLen = len(s) + 1
        have, need = 0, len(t)
        while r < len(s):
            print('hello')
            hashmapS[s[r]]+=1
            if s[r] in hashmapT and hashmapS[s[r]] == hashmapT[s[r]]:
                have+=1
            while have == need:
                print(f"l is {l} and r is {r}")
                if (r - l + 1) < bestLen:
                    res = [l,r]
                    bestLen = r - l + 1
                hashmapS[s[l]]-=1
                if s[l] in hashmapT and hashmapS[s[l]] < hashmapT[s[l]]:
                    have-=1
                l+=1
            r+=1
        return s[res[0]:res[1]+1] if bestLen != len(s) +1 else ""
            


