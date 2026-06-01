class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        topLeft = 0
        done = False
        while len(res) != (ROWS*COLS):
            for i in range(topLeft, COLS - topLeft):
                res.append(matrix[topLeft][i])
            if len(res) == (ROWS*COLS):
                break
            for i in range(topLeft+1, ROWS - topLeft):
                res.append(matrix[i][COLS - topLeft -1])
            if len(res) == (ROWS*COLS):
                break
            for i in range(COLS - 2 - topLeft, -1 + topLeft, -1):
                res.append(matrix[ROWS - topLeft - 1][i])
            for i in range(ROWS - 2 - topLeft, topLeft, -1):
                res.append(matrix[i][topLeft])
            print(res)
            topLeft+=1
        return res