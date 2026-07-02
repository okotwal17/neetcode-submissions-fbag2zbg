class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = set(), set(), set()
        numbers = "123456789"
        for i in range(len(board)):
            for j in range(len(board[0])):
                curElem = board[i][j]
                if curElem not in numbers:
                    continue
                boxIdx = (i//3) * 3 + (j//3)
                if ((i, curElem) in rows or 
                (j, curElem) in cols or 
                (boxIdx, curElem) in boxes):
                    return False
                rows.add((i, curElem))
                cols.add((j, curElem))
                boxes.add((boxIdx, curElem))
        return True