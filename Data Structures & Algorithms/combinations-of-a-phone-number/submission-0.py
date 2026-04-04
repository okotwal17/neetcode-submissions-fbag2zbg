class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        letterMap = {
            '2' : ['a','b','c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        def backtrack(curStr, curIdx):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            letList = letterMap[digits[curIdx]]
            for let in letList:
                curStr+= let
                backtrack(curStr, curIdx + 1)
                curStr = curStr[:-1]
        backtrack("", 0)
        return res