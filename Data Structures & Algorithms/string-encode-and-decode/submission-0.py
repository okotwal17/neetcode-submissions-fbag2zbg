class Solution:

    def encode(self, strs: List[str]) -> str:
        solution=""
        for e in strs:
            solution+=str(len(e))+":"+e
        print(solution)
        return solution
        #6:iojdnf
    def decode(self, s: str) -> List[str]:
        solution = []
        i=0
        while i < len(s):
            print(i)
            strs = ""
            number = 0
            while(s[i]!=":"):
                strs+=s[i]
                i+=1
            print(strs)
            number = int(strs)
            solution.append(s[i+1:i+number+1])
            print(solution[len(solution)-1])
            i+=number+1
            print(i)
        return solution