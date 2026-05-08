class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = dict()
        for i in range(len(s)):
            hashMap[s[i]] = i
        size, end = 0, hashMap[s[0]]
        res = []
        for i in range(len(s)):
            print(s[i], size, end)
            if i == end:
                res.append(size + 1)
                size = 0
                end = hashMap[s[i + 1]] if i + 1 < len(s) else -1
                continue
            size+=1
            end = max(end, hashMap[s[i]])
        return res
            