class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        top, bottom = 0, ROWS
        left, right = 0, COLS
        while len(res) != (ROWS * COLS):
            #Cols changing
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            #Rows changing
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if len(res) == (ROWS * COLS):
                break
            #Cols changing
            for i in range(right - 1, left - 1, -1):
                print(bottom, i)
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            #Rows changing
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res