class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(x,y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] != 1 or (x,y) in visited:
                return 0
            visited.add((x,y))
            return 1 + dfs(x+1,y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea