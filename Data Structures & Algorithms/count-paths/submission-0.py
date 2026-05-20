class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            tempList = []
            for j in range(n):
                tempList.append(1)
            grid.append(tempList)
        print(grid)
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j-1]
        return grid[m-1][n-1]

            
