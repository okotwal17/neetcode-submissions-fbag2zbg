class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = [0] * 26
        second = [0] * 26
        for a in s:
            first[ord(a)-ord('a')]+=1
        for b in t:
            second[ord(b)-ord('a')]+=1
        return tuple(first) == tuple(second)