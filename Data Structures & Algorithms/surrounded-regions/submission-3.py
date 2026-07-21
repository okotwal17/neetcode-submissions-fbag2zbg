class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
            or (r,c) in visited or board[r][c] == "X"):
                return
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        #ROWS
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS - 1, i)
        #COLS
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)
        #X out
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = "X"
