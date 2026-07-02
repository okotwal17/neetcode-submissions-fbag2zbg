class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res+=str(len(string))+"#"+string
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        res = []
        while i < len(s):
            length = ""
            #Getting the length of string
            while s[i] != "#":
                length+=s[i]
                i+=1
            i+=1
            length = int(length)
            res.append(s[i: i + length])
            i+=length
        return res
