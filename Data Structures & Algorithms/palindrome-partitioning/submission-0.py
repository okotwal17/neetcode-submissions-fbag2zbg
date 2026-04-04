class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(curList, j):
            if j >= len(s):
                res.append(curList[:])
                return
            for i in range(j, len(s)):
                if self.isPalindrome(s, j, i):
                    curList.append(s[j:i + 1])
                    backtrack(curList, i + 1)
                    curList.pop()
        backtrack([], 0)
        return res
        
    def isPalindrome(self, s: str, l : int, r : int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True