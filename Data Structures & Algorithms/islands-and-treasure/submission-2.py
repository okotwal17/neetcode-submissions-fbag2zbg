from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]           
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row in range(rows) and col in range(cols)
                    and (row, col) not in visited and grid[row][col] != -1):
                        visited.add((row,col))
                        q.append((row,col))
                        grid[row][col] = grid[r][c] + 1

