class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for a in strs:
            res+=str(len(a)) + "#" + a
        return res
    # 4#neet4#code
    def decode(self, s: str) -> List[str]:
        i = 0;
        res = []
        while(i < len(s)):
            num = ""
            while(s[i]!='#'):
                num+=s[i]
                i+=1
            i+=1
            strToNum = int(num)
            print(strToNum)
            res.append(s[i:i+strToNum])
            i+=strToNum
        return res

