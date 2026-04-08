class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""
        for i in s:
            if(i.isalpha()):
                newstr+=i
        newstr = newstr.lower()
        print(len(newstr)-1)
        lp, rp = 0,len(newstr)-1
        print(f"lp is {lp} and rp is {rp}")
        while(lp<=rp):
            if(newstr[lp] != newstr[rp]):
                return False
            print(f"lp is {lp} and rp is {rp}")
            lp+=1
            rp-=1
        return True