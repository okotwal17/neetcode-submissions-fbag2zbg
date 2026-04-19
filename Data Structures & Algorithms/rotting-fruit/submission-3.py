from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes, fresh = 0,0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))            
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row in range(rows) and col in range(cols) and (row,col) not in visited and grid[row][col] !=0:
                        q.append((row,col))
                        visited.add((row,col))
                        fresh-=1
            minutes+=1
        return minutes if fresh == 0 else -1
