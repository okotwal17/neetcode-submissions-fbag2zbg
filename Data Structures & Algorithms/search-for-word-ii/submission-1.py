class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, word, node):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
            or (r,c) in visit or board[r][c] not in node.children):
                return
            visit.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            for dr, dc in directions:
                dfs(dr + r, dc + c, word, node)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, "", root)
        return list(res)