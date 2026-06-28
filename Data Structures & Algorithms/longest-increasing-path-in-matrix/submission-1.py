class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        def dfs(r,c,prevVal):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or prevVal >= matrix[r][c]):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + dfs(r+dr, c+dc, matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        LIP = -1
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r,c,-1))
        return LIP
            
            