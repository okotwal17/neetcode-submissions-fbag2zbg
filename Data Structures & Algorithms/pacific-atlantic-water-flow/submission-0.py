class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        #r,c
        def dfs(x, y, prevVal, curSet):
            if x < 0 or y < 0 or x >= rows or y>=cols or heights[x][y] < prevVal or (x,y) in curSet:
                return
            curSet.add((x,y))

            newVal = heights[x][y]
            dfs(x+1, y, newVal, curSet)
            dfs(x-1, y, newVal, curSet)
            dfs(x, y+1, newVal, curSet)
            dfs(x, y-1, newVal, curSet)
        pacific = set()
        atlantic = set()
        for i in range(cols):
            dfs(0,i, heights[0][i],pacific)
            dfs(rows-1,i, heights[rows-1][i],atlantic)
        for i in range(rows):
            dfs(i,0, heights[i][0],pacific)
            dfs(i,cols-1, heights[i][cols-1],atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res


