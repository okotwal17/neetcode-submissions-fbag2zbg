class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificVisited, atlanticVisited = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r, c, prevHeight, oceanSet):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
            or (r,c) in oceanSet or heights[r][c] < prevHeight):
                return
            oceanSet.add((r,c))
            prevHeight = heights[r][c]
            for dr, dc in directions:
                dfs(r + dr, c + dc, prevHeight, oceanSet)
        
        #Pacific
        for i in range(COLS):
            dfs(0, i, float("-inf"), pacificVisited)
        for i in range(ROWS):
            dfs(i, 0, float("-inf"), pacificVisited)
        #Atlantic
        for i in range(COLS):
            dfs(ROWS - 1, i, float("-inf"), atlanticVisited)
        for i in range(ROWS):
            dfs(i, COLS - 1, float("-inf"), atlanticVisited)
        #Both
        res = []
        for elem in pacificVisited:
            if elem in atlanticVisited:
                res.append(list(elem))
        return res
