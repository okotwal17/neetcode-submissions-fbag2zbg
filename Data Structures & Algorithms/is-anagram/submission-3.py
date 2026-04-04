from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDictionary = defaultdict(int)
        secondDictionary = defaultdict(int)
        for a in s:
            firstDictionary[a]+=1
        for b in t:
            secondDictionary[b]+=1
        return firstDictionary == secondDictionary
