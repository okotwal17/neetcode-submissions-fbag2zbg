class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        freshFruit = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruit += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        time = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            print(q)
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if (newR >= 0 and newC >= 0 and 
                    newR < ROWS and newC < COLS 
                    and (newR,newC) not in visited and grid[newR][newC] == 1):
                        q.append((newR,newC))
                        visited.add((newR,newC))
                        freshFruit -= 1
            if q:
                time += 1
            print(q, time)
        return time if freshFruit == 0 else -1
