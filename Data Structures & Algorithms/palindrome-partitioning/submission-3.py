class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(j, path):
            if j == len(s):
                res.append(path[:])
                return
            for i in range(j, len(s)):
                if self.isPalindrome(s[j: i + 1]):
                    path.append(s[j: i + 1])
                    backtrack(i + 1, path)
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