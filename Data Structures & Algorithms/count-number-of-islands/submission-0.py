class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(x, y):
            print(x,y)
            if y >= cols or y < 0 or x < 0 or x >= rows or grid[x][y] != "1":
                return
            grid[x][y] = "#"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count+=1
        return count