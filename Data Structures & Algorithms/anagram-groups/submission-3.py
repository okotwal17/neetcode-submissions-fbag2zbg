from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            freq = [0] * 26
            for c in string:
                idx = ord(c) - ord('a')
                freq[idx]+=1
            hashmap[tuple(freq)].append(string)
        return list(hashmap.values())
            