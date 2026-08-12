class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroCol, zeroRow = False, False
        ROWS, COLS = len(matrix), len(matrix[0])
        #Counting our zeroes essentially
        for i in range(COLS):
            if matrix[0][i] == 0:
                zeroRow = True
                break
        for i in range(ROWS):
            if matrix[i][0] == 0:
                zeroCol = True
                break
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        #Setting appropriate stuff to zero
        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for j in range(1, COLS):
                    matrix[i][j] = 0
        
        for i in range(1, COLS):
            if matrix[0][i] == 0:
                for j in range(1, ROWS):
                    matrix[j][i] = 0
        
        if zeroRow:
            for i in range(COLS):
                matrix[0][i] = 0
        if zeroCol:
            for i in range(ROWS):
                matrix[i][0] = 0

