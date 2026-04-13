from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, count = 0,0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh-=1
            count+=1
        return count if fresh==0 else -1
                
