class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r, c):
            if(r < 0 or c < 0 
            or r == ROWS or c == COLS 
            or (r,c) in visited or grid[r][c] == 0):
                return 0
            curArea = 1
            visited.add((r,c))
            for dr, dc in directions:
                curArea += dfs(r + dr, c + dc)
            return curArea
    
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea
