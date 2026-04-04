class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r  = l + 1, r - 1
            return True

        def backtrack(curList, i):
            if i >= len(s):
                res.append(curList[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    curList.append(s[i : j + 1])
                    backtrack(curList, j + 1)
                    curList.pop()
        backtrack([],0)
        return res
    
        