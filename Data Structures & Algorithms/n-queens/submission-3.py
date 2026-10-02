class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]
        def backtrack(curBoard, numQueens, r):
            if numQueens == n:
                temp = board.copy()
                res.append(["".join(temp[i]) for i in range(len(temp))])
                return 
            for c in range(n):
                if (c not in col and 
                r - c not in negDiag and r + c not in posDiag):
                    curBoard[r][c] = "Q"
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    backtrack(curBoard, numQueens + 1, r + 1)
                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    curBoard[r][c] = "."
        backtrack(board, 0, 0)
        return res