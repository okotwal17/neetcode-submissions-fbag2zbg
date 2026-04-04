from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for c in strs:
            count = [0] * 26
            for chars in c:
                count[ord(chars) - ord('a')] += 1
            hashmap[tuple(count)].append(c)
        return list(hashmap.values())