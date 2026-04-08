class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(curString, curRow, curCol):
            if curString == word:
                return True
            if len(curString) >= len(word):
                return False
            
            if curRow + 1 < len(board) and backtrack(curString + board[curRow + 1][curCol], curRow + 1, curCol):
                return True
            elif curRow - 1 >= 0 and backtrack(curString + board[curRow - 1][curCol], curRow - 1, curCol):
                return True
            elif curCol + 1 < len(board) and backtrack(curString + board[curRow][curCol + 1], curRow, curCol + 1):
                return True
            elif curCol - 1 >= 0 and backtrack(curString + board[curRow][curCol - 1], curRow, curCol - 1):
                return True
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack("", i, j):
                    return True
        return False
