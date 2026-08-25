class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setColZero, setRowZero = False, False
        ROWS, COLS = len(matrix), len(matrix[0])
        #Setting flags up
        for r in range(ROWS):
            if matrix[r][0] == 0:
                setColZero = True
                break
        for c in range(COLS):
            if matrix[0][c] == 0:
                setRowZero = True
                break
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        #Working on those flags
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if setColZero:
            for r in range(ROWS):
                matrix[r][0] = 0
        if setRowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        