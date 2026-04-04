class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        delimiter = "#"
        for s in strs:
            n = len(s)
            res+=str(n)+delimiter+s
        return res
    
    #4#neet4#code
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while(i < len(s)):
            num = ""
            while(s[i] != "#"):
                num+=s[i]
                i+=1
            #At this point in time, our i will be at the #so we need the next num letters
            numToInt = int(num)
            i+=1
            res.append(s[i:i+numToInt])
            i+=numToInt
        return res