class Solution:

    def encode(self, strs: List[str]) -> str:
        solution=""
        for e in strs:
            solution+=str(len(e))+":"+e
        return solution
        #6:iojdnf
    def decode(self, s: str) -> List[str]:
        solution = []
        i=0
        while i < len(s):
            strs = ""
            number = 0
            while(s[i]!=":"):
                strs+=s[i]
                i+=1
            number = int(strs)
            solution.append(s[i+1:i+number+1])
            i+=number+1
        return solution