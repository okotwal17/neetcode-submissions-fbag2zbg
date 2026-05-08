class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = dict()
        for i in range(len(s)):
            hashMap[s[i]] = i
        size, end = 0, 0
        res = []
        for i in range(len(s)):
            size+=1
            end = max(end, hashMap[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res
            