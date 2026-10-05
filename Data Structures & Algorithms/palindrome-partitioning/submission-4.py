class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i,path):
            if i >= len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if self.isPalindrome(temp):
                    path.append(temp)
                    dfs(j+1, path)
                    path.pop()
        dfs(0, [])
        return res
    def isPalindrome(self,string):
        l, r = 0, len(string) - 1
        while l <= r: 
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True