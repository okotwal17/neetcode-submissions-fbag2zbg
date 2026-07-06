class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1) - 1
        firstFreq = [0] * 26
        secondFreq = [0] * 26
        #Frequency of characters in first word and window of second word
        for i in range(len(s1)):
            firstFreq[ord(s1[i]) - ord('a')] += 1
            secondFreq[ord(s2[i]) - ord('a')] += 1

        while r < len(s2):
            if firstFreq == secondFreq:
                return True
            secondFreq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                secondFreq[ord(s2[r]) - ord('a')] += 1
        return False
