class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        def dfs(i, j, prevVal):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 0
            if matrix[i][j] <= prevVal:
                return 0
            if (i, j) in dp:
                return dp[(i,j)]
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + dfs(dr+i, dc+j, matrix[i][j]))
            dp[(i, j)] = res
            return res
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        print(dp)
        return max(dp.values())
