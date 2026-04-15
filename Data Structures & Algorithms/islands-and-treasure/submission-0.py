from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        

        def addRoom(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == -1 or (x,y) in visited or grid[x][y] == 0:
                return
            visited.add((x,y))
            q.append((x,y)) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                grid[x][y] = dist
                addRoom(x+1,y)
                addRoom(x-1,y)
                addRoom(x,y+1)
                addRoom(x,y-1)
            dist+=1
        
                

        