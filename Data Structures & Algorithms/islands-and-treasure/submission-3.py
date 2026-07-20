class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        INF = 2147483647
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if (newR >= 0 and newC >= 0 and newR < ROWS and newC < COLS
                    and grid[newR][newC] == 2147483647):
                        grid[newR][newC] = 1 + grid[r][c]
                        q.append((r + dr, c + dc))
        

