class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res1 = [0] * 26
        res2 = [0] * 26
        l,r = 0,0

        for i in s1:
            res1[ord(i) - ord('a')]+=1
        print(res1)

        while r<len(s2):
            if res1[ord(s2[r]) - ord('a')]>=1:
                res2[ord(s2[r]) - ord('a')]+=1
                r+=1
            elif res1 == res2:
                return True
            else:
                res2 = [0] * 26
                r+=1
                l = r
        print(res2)
        return res1 == res2