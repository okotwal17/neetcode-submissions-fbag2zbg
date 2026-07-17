class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(i, path):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s[i : j + 1]):
                    path.append(s[i:j + 1])
                    backtrack(j + 1, path)
                    path.pop()
        backtrack(0, [])
        return res

        
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    