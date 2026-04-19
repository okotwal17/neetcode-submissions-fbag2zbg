class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        def dfs(r,c, prevVal, ocean):
            if r not in range(rows) or c not in range(cols) or prevVal > heights[r][c] or (r,c) in ocean:
                return
            ocean.add((r,c))
            dfs(r+1,c, heights[r][c], ocean)
            dfs(r-1,c, heights[r][c], ocean)
            dfs(r,c+1, heights[r][c], ocean)
            dfs(r,c-1, heights[r][c], ocean)
        
        for row in range(rows):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, cols -1, heights[row][cols-1], atlantic)
        for col in range(cols):
            dfs(0, col, heights[0][col], pacific)
            dfs(rows - 1, col, heights[rows-1][col], atlantic)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                temp = (r,c)
                if temp in atlantic and temp in pacific:
                    res.append([r,c])
        return res
