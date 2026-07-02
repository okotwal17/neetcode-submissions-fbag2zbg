class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstFreq, secondFreq = [0] * 26, [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            firstFreq[idx]+=1
        for c in t:
            idx = ord(c) - ord('a')
            secondFreq[idx]+=1
        return firstFreq == secondFreq