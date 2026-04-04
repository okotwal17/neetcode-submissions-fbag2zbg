class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars,tChars = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sChars[s[i]] = 1+sChars.get(s[i],0)
            tChars[t[i]] = 1+tChars.get(t[i],0)
        return sChars == tChars