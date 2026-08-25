class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                aboveSum = self.matrix[r][c + 1]
                prefix += matrix[r][c]
                self.matrix[r + 1][c + 1] = prefix + aboveSum
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #Bottomleft, top right
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        res = self.matrix[r2][c2]
        leftSum = self.matrix[r2][c1 - 1]
        topSum = self.matrix[r1 - 1][c2]
        topLeft = self.matrix[r1 - 1][c1 - 1]
        return res - leftSum - topSum + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)