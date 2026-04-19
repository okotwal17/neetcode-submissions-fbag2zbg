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
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                if r + 1 < rows and (r+1,c) not in visited and grid[r+1][c] != 0:
                    q.append((r+1,c))
                    visited.add((r+1,c))
                    fresh-=1
                if r - 1 >= 0 and (r-1,c) not in visited and grid[r-1][c] != 0:
                    q.append((r-1,c))
                    visited.add((r-1,c))
                    fresh-=1
                if c + 1 < cols and (r,c+1) not in visited and grid[r][c+1] != 0:
                    q.append((r,c + 1))
                    visited.add((r,c+1))
                    fresh-=1
                if c - 1 >= 0 and (r,c-1) not in visited and grid[r][c-1] != 0:
                    q.append((r,c - 1))
                    visited.add((r,c-1))
                    fresh-=1
            minutes+=1
    
        return minutes if fresh == 0 else -1
