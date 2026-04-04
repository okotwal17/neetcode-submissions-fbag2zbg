class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstList = [0] * 26
        secondList = [0] * 26
        for first in s:
            firstList[ord(first) - ord('a')]+=1
        for second in t:
            secondList[ord(second) - ord('a')]+=1
        return firstList == secondList
